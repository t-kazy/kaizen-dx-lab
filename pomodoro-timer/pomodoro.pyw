"""
ポモドーロタイマー
- このファイルをダブルクリックするだけで起動します
- Python 3.x が必要です（https://www.python.org/ から無料でインストールできます）
"""

import tkinter as tk
from tkinter import font as tkfont
import math
import threading
import winsound  # Windows 標準の音声ライブラリ

# ─────────────────────────────────────────
#  設定・定数
# ─────────────────────────────────────────

WINDOW_W = 240
WINDOW_H = 310
RING_SIZE = 160          # キャンバスの一辺
RING_CENTER = RING_SIZE // 2
RADIUS = 68
RING_WIDTH = 8

THEMES = {
    "work":  {"bg": "#1e1e2e", "surface": "#2a2a3e", "accent": "#f38ba8", "fg": "#cdd6f4", "label": "FOCUS"},
    "break": {"bg": "#1a2e1a", "surface": "#253825", "accent": "#a6e3a1", "fg": "#cdd6f4", "label": "SHORT BREAK"},
    "long":  {"bg": "#1e1a2e", "surface": "#2e2538", "accent": "#fab387", "fg": "#cdd6f4", "label": "LONG BREAK"},
}

DEFAULT_MINUTES = {"work": 25, "break": 5, "long": 15}


# ─────────────────────────────────────────
#  メインアプリ
# ─────────────────────────────────────────

class PomodoroApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("🍅 Pomodoro")
        self.root.geometry(f"{WINDOW_W}x{WINDOW_H}")
        self.root.resizable(False, False)
        self.root.attributes("-topmost", True)   # 常に最前面

        # 状態
        self.mode         = "work"
        self.minutes      = dict(DEFAULT_MINUTES)
        self.total_sec    = self.minutes["work"] * 60
        self.remain_sec   = self.total_sec
        self.running      = False
        self.done_count   = 0
        self._after_id    = None
        self.topmost      = True

        self._build_ui()
        self._apply_theme()
        self._update_display()

    # ── UI構築 ────────────────────────────

    def _build_ui(self):
        root = self.root

        # ── モードバー
        self.mode_frame = tk.Frame(root, height=28)
        self.mode_frame.pack(fill="x")
        self.mode_frame.pack_propagate(False)

        self.tab_btns = {}
        for m, text in [("work", "作業"), ("break", "休憩"), ("long", "長休憩")]:
            b = tk.Button(
                self.mode_frame, text=text, relief="flat", bd=0,
                font=("Meiryo", 9, "bold"), cursor="hand2",
                command=lambda m=m: self.switch_mode(m),
            )
            b.pack(side="left", expand=True, fill="both")
            self.tab_btns[m] = b

        # ── キャンバス（円形タイマー）
        self.canvas = tk.Canvas(
            root, width=RING_SIZE, height=RING_SIZE,
            highlightthickness=0,
        )
        self.canvas.pack(pady=(8, 0))

        # 背景トラック
        self._draw_arc("track", 0, 359.99, width=RING_WIDTH)
        # プログレス
        self._draw_arc("prog",  0, 359.99, width=RING_WIDTH)

        # 時刻テキスト
        self.time_font  = tkfont.Font(family="Segoe UI", size=28, weight="bold")
        self.label_font = tkfont.Font(family="Segoe UI", size=8)
        self.canvas.create_text(
            RING_CENTER, RING_CENTER - 6,
            text="25:00", font=self.time_font, fill="#cdd6f4", tags="time_text",
        )
        self.canvas.create_text(
            RING_CENTER, RING_CENTER + 18,
            text="FOCUS", font=self.label_font, fill="#888aaa", tags="mode_text",
        )

        # ── コントロールボタン
        ctrl = tk.Frame(root)
        ctrl.pack(pady=6)

        btn_cfg = dict(relief="flat", bd=0, font=("Segoe UI", 14), cursor="hand2",
                       width=2, height=1)

        self.reset_btn = tk.Button(ctrl, text="⏮", command=self.reset_timer, **btn_cfg)
        self.reset_btn.grid(row=0, column=0, padx=4)

        self.start_btn = tk.Button(ctrl, text="▶", command=self.toggle_timer, **btn_cfg)
        self.start_btn.grid(row=0, column=1, padx=4)

        self.skip_btn = tk.Button(ctrl, text="⏭", command=self.skip_session, **btn_cfg)
        self.skip_btn.grid(row=0, column=2, padx=4)

        # ── トマトカウンター
        self.tomato_var = tk.StringVar(value="")
        tomato_lbl = tk.Label(root, textvariable=self.tomato_var,
                              font=("Segoe UI", 11))
        tomato_lbl.pack(pady=(0, 4))
        self.tomato_lbl = tomato_lbl

        # ── 下部ツールバー（常に最前面 トグル ＋ 設定）
        bar = tk.Frame(root)
        bar.pack(fill="x", padx=6, pady=(0, 4))

        self.pin_btn = tk.Button(
            bar, text="📌 最前面ON", relief="flat", bd=0,
            font=("Meiryo", 8), cursor="hand2",
            command=self.toggle_topmost,
        )
        self.pin_btn.pack(side="left")

        cfg_btn = tk.Button(
            bar, text="⚙ 設定", relief="flat", bd=0,
            font=("Meiryo", 8), cursor="hand2",
            command=self.open_settings,
        )
        cfg_btn.pack(side="right")
        self.cfg_btn = cfg_btn

        # ── キーボードショートカット
        root.bind("<space>", lambda e: self.toggle_timer())
        root.bind("<r>",     lambda e: self.reset_timer())
        root.bind("<R>",     lambda e: self.reset_timer())

    def _draw_arc(self, tag, start, extent, width=RING_WIDTH):
        pad = width
        x0, y0 = pad, pad
        x1, y1 = RING_SIZE - pad, RING_SIZE - pad
        self.canvas.create_arc(
            x0, y0, x1, y1,
            start=start, extent=extent,
            style="arc", width=width, tags=tag,
        )

    # ── テーマ適用 ────────────────────────

    def _apply_theme(self):
        t  = THEMES[self.mode]
        bg = t["bg"]
        ac = t["accent"]
        fg = t["fg"]
        sf = t["surface"]

        self.root.configure(bg=bg)
        self.mode_frame.configure(bg=bg)
        self.canvas.configure(bg=bg)

        # タブボタン
        for m, b in self.tab_btns.items():
            if m == self.mode:
                b.configure(bg=sf, fg=fg)
            else:
                b.configure(bg=bg, fg="#55576a")

        # リング
        self.canvas.itemconfig("track", outline="#2e2e4e")
        self.canvas.itemconfig("prog",  outline=ac)

        # テキスト
        self.canvas.itemconfig("time_text", fill=fg)
        self.canvas.itemconfig("mode_text", fill="#888aaa")

        # コントロールボタン
        for b in (self.reset_btn, self.skip_btn):
            b.configure(bg=sf, fg=fg, activebackground=bg, activeforeground=fg)
        self.start_btn.configure(bg=ac, fg=bg, activebackground=ac, activeforeground=bg)

        # トマト・下部バー
        self.tomato_lbl.configure(bg=bg)
        self.canvas.master.configure(bg=bg)
        for w in self.root.winfo_children():
            try:
                w.configure(bg=bg)
            except Exception:
                pass

        self.pin_btn.configure(bg=bg, fg="#666888", activebackground=bg)
        self.cfg_btn.configure(bg=bg, fg="#666888", activebackground=bg)

    # ── モード切替 ────────────────────────

    def switch_mode(self, mode):
        self._stop()
        self.mode      = mode
        self.total_sec = self.minutes[mode] * 60
        self.remain_sec = self.total_sec
        self.canvas.itemconfig("mode_text", text=THEMES[mode]["label"])
        self._apply_theme()
        self._update_display()

    # ── タイマー操作 ──────────────────────

    def toggle_timer(self):
        if self.running:
            self._pause()
        else:
            self._start()

    def _start(self):
        self.running = True
        self.start_btn.configure(text="⏸")
        self._tick()

    def _pause(self):
        self.running = False
        self.start_btn.configure(text="▶")
        if self._after_id:
            self.root.after_cancel(self._after_id)

    def _stop(self):
        self._pause()
        self.remain_sec = self.total_sec

    def reset_timer(self):
        self._stop()
        self._update_display()
        self._flash_message("リセット")

    def skip_session(self):
        self._stop()
        self._on_complete(auto=False)

    # ── 毎秒処理 ──────────────────────────

    def _tick(self):
        if not self.running:
            return
        self.remain_sec -= 1
        self._update_display()
        if self.remain_sec <= 0:
            self._on_complete(auto=True)
        else:
            self._after_id = self.root.after(1000, self._tick)

    # ── セッション完了 ────────────────────

    def _on_complete(self, auto: bool):
        self._stop()
        if self.mode == "work":
            self.done_count += 1
            self._render_tomatoes()
            if auto:
                self._play_bell()
            long_break = self.done_count % 4 == 0
            next_mode  = "long" if long_break else "break"
            msg = ("長い休憩へ！" if long_break else "休憩しましょう！") if auto else ""
            if msg:
                self._flash_message(msg)
            self.root.after(500, lambda: self.switch_mode(next_mode))
        else:
            if auto:
                self._play_bell()
                self._flash_message("休憩終了！")
            self.root.after(500, lambda: self.switch_mode("work"))

    # ── 表示更新 ──────────────────────────

    def _update_display(self):
        m = self.remain_sec // 60
        s = self.remain_sec % 60
        self.canvas.itemconfig("time_text", text=f"{m:02d}:{s:02d}")

        # プログレスアーク
        ratio   = self.remain_sec / self.total_sec if self.total_sec else 1
        extent  = -359.99 * ratio   # 負の値で時計回り
        # 一度削除して再描画（extent 更新が楽なため）
        self.canvas.delete("prog")
        pad = RING_WIDTH
        self.canvas.create_arc(
            pad, pad, RING_SIZE - pad, RING_SIZE - pad,
            start=90, extent=extent,
            style="arc", width=RING_WIDTH,
            outline=THEMES[self.mode]["accent"], tags="prog",
        )

    def _render_tomatoes(self):
        total   = min(max(8, self.done_count + 1), 8)
        tomatos = ""
        for i in range(total):
            if i < self.done_count:
                tomatos += "🍅"
            else:
                tomatos += "🔲"
        extra = f" +{self.done_count - 8}" if self.done_count > 8 else ""
        self.tomato_var.set(tomatos + extra)

    # ── 最前面トグル ──────────────────────

    def toggle_topmost(self):
        self.topmost = not self.topmost
        self.root.attributes("-topmost", self.topmost)
        self.pin_btn.configure(
            text="📌 最前面ON" if self.topmost else "📌 最前面OFF"
        )

    # ── 設定ウィンドウ ────────────────────

    def open_settings(self):
        t = THEMES[self.mode]
        win = tk.Toplevel(self.root)
        win.title("設定")
        win.resizable(False, False)
        win.attributes("-topmost", True)
        win.configure(bg=t["bg"])

        labels = [("作業時間（分）", "work"), ("短い休憩（分）", "break"), ("長い休憩（分）", "long")]
        entries = {}

        for i, (lbl_text, key) in enumerate(labels):
            tk.Label(win, text=lbl_text, bg=t["bg"], fg=t["fg"],
                     font=("Meiryo", 9)).grid(row=i, column=0, padx=12, pady=4, sticky="w")
            var = tk.IntVar(value=self.minutes[key])
            e = tk.Entry(win, textvariable=var, width=5, justify="center",
                         bg=t["surface"], fg=t["fg"], insertbackground=t["fg"],
                         relief="flat", font=("Segoe UI", 10))
            e.grid(row=i, column=1, padx=12, pady=4)
            entries[key] = var

        def save():
            for key, var in entries.items():
                try:
                    v = int(var.get())
                    if 1 <= v <= 120:
                        self.minutes[key] = v
                except ValueError:
                    pass
            self.switch_mode(self.mode)
            win.destroy()

        tk.Button(
            win, text="保存", command=save,
            bg=t["accent"], fg=t["bg"], relief="flat",
            font=("Meiryo", 9, "bold"), cursor="hand2", width=8,
        ).grid(row=len(labels), column=0, columnspan=2, pady=8)

    # ── メッセージフラッシュ ──────────────

    def _flash_message(self, msg: str):
        """タイトルバーに一時メッセージを表示"""
        self.root.title(f"🍅 {msg}")
        self.root.after(2500, lambda: self.root.title("🍅 Pomodoro"))

    # ── ベル音 ────────────────────────────

    def _play_bell(self):
        def _beep():
            for freq in [880, 880, 1000]:
                try:
                    winsound.Beep(freq, 200)
                except Exception:
                    pass
        threading.Thread(target=_beep, daemon=True).start()


# ─────────────────────────────────────────
#  起動
# ─────────────────────────────────────────

if __name__ == "__main__":
    root = tk.Tk()
    app  = PomodoroApp(root)
    root.mainloop()
