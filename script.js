// ============================================
// Customer Satisfaction Survey - Logic
// ============================================

let currentStep = 1;
const totalSteps = 5;

const answers = {
  satisfaction: null,
  categories: {
    quality: 0,
    speed: 0,
    communication: 0,
    cost: 0,
  },
  nps: null,
  feedback: '',
};

// --- Navigation ---

function updateProgress() {
  const fill = document.getElementById('progressFill');
  const text = document.getElementById('progressText');
  const pct = (currentStep / totalSteps) * 100;
  fill.style.width = pct + '%';
  text.textContent = currentStep + ' / ' + totalSteps;
}

function showStep(step) {
  document.querySelectorAll('.step').forEach(function (el) {
    el.classList.remove('active');
  });
  var target = document.querySelector('[data-step="' + step + '"]');
  if (target) {
    target.classList.add('active');
  }
  updateProgress();
}

function nextStep() {
  if (currentStep < totalSteps) {
    currentStep++;
    showStep(currentStep);

    if (currentStep === totalSteps) {
      renderSummary();
    }
  }
}

function prevStep() {
  if (currentStep > 1) {
    currentStep--;
    showStep(currentStep);
  }
}

// --- Rating Cards (Q1) ---

function selectRating(el) {
  var group = el.closest('.rating-group');
  group.querySelectorAll('.rating-card').forEach(function (card) {
    card.classList.remove('selected');
  });
  el.classList.add('selected');
  answers.satisfaction = parseInt(el.dataset.value, 10);

  var nextBtn = document.getElementById('step2Next');
  if (nextBtn) {
    nextBtn.disabled = false;
  }
}

// --- Star Ratings (Q2) ---

function selectStar(el) {
  var container = el.closest('.star-rating');
  var value = parseInt(el.dataset.value, 10);
  var category = container.dataset.category;

  answers.categories[category] = value;

  container.querySelectorAll('.star').forEach(function (star) {
    var v = parseInt(star.dataset.value, 10);
    if (v <= value) {
      star.classList.add('active');
    } else {
      star.classList.remove('active');
    }
  });
}

// --- NPS (Q3) ---

function selectNps(el) {
  var group = document.getElementById('npsGroup');
  group.querySelectorAll('.nps-btn').forEach(function (btn) {
    btn.classList.remove('selected');
  });
  el.classList.add('selected');
  answers.nps = parseInt(el.dataset.value, 10);
}

// --- Summary ---

function satisfactionLabel(val) {
  var labels = {
    5: 'とても満足',
    4: '満足',
    3: '普通',
    2: 'やや不満',
    1: '不満',
  };
  return labels[val] || '未回答';
}

function starsString(count) {
  var filled = '';
  var empty = '';
  for (var i = 0; i < count; i++) filled += '★';
  for (var i = count; i < 5; i++) empty += '☆';
  return filled + empty;
}

function renderSummary() {
  // Capture free text before rendering
  var feedbackEl = document.getElementById('feedback');
  if (feedbackEl) {
    answers.feedback = feedbackEl.value;
  }

  var card = document.getElementById('summaryCard');
  var rows = '';

  rows +=
    '<div class="summary-row">' +
    '<span class="summary-label">総合満足度</span>' +
    '<span class="summary-value">' +
    satisfactionLabel(answers.satisfaction) +
    '</span>' +
    '</div>';

  var catNames = {
    quality: '品質',
    speed: '対応スピード',
    communication: 'コミュニケーション',
    cost: 'コストパフォーマンス',
  };

  for (var key in catNames) {
    rows +=
      '<div class="summary-row">' +
      '<span class="summary-label">' +
      catNames[key] +
      '</span>' +
      '<span class="summary-value">' +
      starsString(answers.categories[key]) +
      '</span>' +
      '</div>';
  }

  rows +=
    '<div class="summary-row">' +
    '<span class="summary-label">おすすめ度 (NPS)</span>' +
    '<span class="summary-value">' +
    (answers.nps !== null ? answers.nps + ' / 10' : '未回答') +
    '</span>' +
    '</div>';

  card.innerHTML = rows;
}

// --- Reset ---

function resetForm() {
  currentStep = 1;
  answers.satisfaction = null;
  answers.categories = { quality: 0, speed: 0, communication: 0, cost: 0 };
  answers.nps = null;
  answers.feedback = '';

  // Clear UI selections
  document.querySelectorAll('.rating-card').forEach(function (el) {
    el.classList.remove('selected');
  });
  document.querySelectorAll('.star').forEach(function (el) {
    el.classList.remove('active');
  });
  document.querySelectorAll('.nps-btn').forEach(function (el) {
    el.classList.remove('selected');
  });

  var feedbackEl = document.getElementById('feedback');
  if (feedbackEl) feedbackEl.value = '';

  var nextBtn = document.getElementById('step2Next');
  if (nextBtn) nextBtn.disabled = true;

  showStep(1);
}

// --- Init ---
updateProgress();
