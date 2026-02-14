// ===== Survey State =====
const TOTAL_QUESTIONS = 5;
let currentStep = 0;
const totalSteps = 7; // welcome + 5 questions + thank you

const answers = {
  satisfaction: null,
  features: [],
  nps: null,
  improvement: null,
  feedback: '',
};

// ===== Initialize =====
document.addEventListener('DOMContentLoaded', () => {
  buildProgressDots();
  updateProgress();
});

// ===== Progress =====
function buildProgressDots() {
  const container = document.getElementById('progressSteps');
  for (let i = 0; i < totalSteps; i++) {
    const dot = document.createElement('div');
    dot.className = 'progress-dot';
    if (i === 0) dot.classList.add('active');
    container.appendChild(dot);
  }
}

function updateProgress() {
  const fill = document.getElementById('progressFill');
  const pct = (currentStep / (totalSteps - 1)) * 100;
  fill.style.width = pct + '%';

  const dots = document.querySelectorAll('.progress-dot');
  dots.forEach((dot, i) => {
    dot.classList.remove('active', 'completed');
    if (i === currentStep) dot.classList.add('active');
    else if (i < currentStep) dot.classList.add('completed');
  });
}

// ===== Navigation =====
function showStep(index) {
  document.querySelectorAll('.step').forEach((el) => {
    el.classList.remove('active');
  });
  const target = document.querySelector(`.step[data-step="${index}"]`);
  if (target) {
    target.classList.remove('active');
    // Force reflow for re-triggering the animation
    void target.offsetWidth;
    target.classList.add('active');
  }
  currentStep = index;
  updateProgress();
}

function nextStep() {
  if (currentStep < totalSteps - 1) {
    showStep(currentStep + 1);
  }
}

function prevStep() {
  if (currentStep > 0) {
    showStep(currentStep - 1);
  }
}

// ===== Emoji Satisfaction =====
function selectEmoji(btn) {
  document.querySelectorAll('.emoji-btn').forEach((b) => b.classList.remove('selected'));
  btn.classList.add('selected');
  answers.satisfaction = parseInt(btn.dataset.value, 10);
  document.getElementById('step1Next').disabled = false;
}

// ===== Checkbox (Features) =====
function toggleCheckbox(card) {
  card.classList.toggle('selected');

  answers.features = [];
  document.querySelectorAll('.checkbox-card.selected').forEach((c) => {
    const title = c.querySelector('.checkbox-title').textContent;
    answers.features.push(title);
  });
}

// ===== NPS =====
function selectNps(btn) {
  document.querySelectorAll('.nps-btn').forEach((b) => b.classList.remove('selected'));
  btn.classList.add('selected');
  answers.nps = parseInt(btn.dataset.value, 10);
  document.getElementById('step3Next').disabled = false;
}

// ===== Radio (Improvement) =====
function selectRadio(card) {
  document.querySelectorAll('.radio-card').forEach((c) => c.classList.remove('selected'));
  card.classList.add('selected');
  answers.improvement = card.querySelector('.radio-title').textContent;
  document.getElementById('step4Next').disabled = false;
}

// ===== Textarea =====
function updateCharCount(textarea) {
  document.getElementById('charCount').textContent = textarea.value.length;
  answers.feedback = textarea.value;
}

// ===== Submit =====
function submitSurvey() {
  answers.feedback = document.getElementById('feedbackText').value;
  renderSummary();
  showStep(6);
  console.log('Survey submitted:', JSON.stringify(answers, null, 2));
}

// ===== Summary =====
function renderSummary() {
  const container = document.getElementById('summaryContent');

  const satisfactionLabels = {
    1: '😞 不満',
    2: '😐 やや不満',
    3: '🙂 普通',
    4: '😊 満足',
    5: '🤩 大満足',
  };

  const items = [
    { label: '満足度', value: satisfactionLabels[answers.satisfaction] || '未回答' },
    { label: '利用機能', value: answers.features.length > 0 ? answers.features.join(', ') : '未選択' },
    { label: 'NPS', value: answers.nps !== null ? answers.nps + ' / 10' : '未回答' },
    { label: '改善希望', value: answers.improvement || '未選択' },
    { label: 'フィードバック', value: answers.feedback || '未記入' },
  ];

  container.innerHTML = items
    .map(
      (item) =>
        `<div class="summary-item">
          <span class="summary-label">${item.label}</span>
          <span class="summary-value">${escapeHtml(item.value)}</span>
        </div>`
    )
    .join('');
}

function escapeHtml(str) {
  const div = document.createElement('div');
  div.appendChild(document.createTextNode(str));
  return div.innerHTML;
}
