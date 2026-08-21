---
layout: single
permalink: /about/
author_profile: true
title: "About Me"
header:
  image: "/assets/images/Portfolio_Banner.png"
classes: wide
---

<div class="custom-tabs">

  <input type="radio" id="tab1" name="tabs" checked>
  <label for="tab1">Big Five</label>

  <input type="radio" id="tab2" name="tabs">
  <label for="tab2">VIA Strengths</label>

  <input type="radio" id="tab3" name="tabs">
  <label for="tab3">16PF</label>

  <div class="tab-content" id="content1">
    <h2>Big Five (OCEAN)</h2>
    <canvas id="big5-chart"></canvas>
  </div>

  <div class="tab-content" id="content2">
    <h2>VIA Character Strengths</h2>
    <ul class="via-list">
      <li><button class="via-btn">Creativity</button></li>
      <li><button class="via-btn">Judgment</button></li>
      <li><button class="via-btn">Love of Learning</button></li>
      <li><button class="via-btn">Perspective</button></li>
    </ul>
  </div>

  <div class="tab-content" id="content3">
    <h2>16PF</h2>
    <canvas id="pf16-chart"></canvas>
  </div>

</div>


<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<script>
// BIG FIVE CHART
new Chart(document.getElementById('big5-chart'), {
  type: 'bar',
  data: {
    labels: ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism'],
    datasets: [{
      label: 'Score',
      data: [99, 61, 38, 74, 14],
      backgroundColor: '#6a4cff'
    }]
  },
  options: {
    indexAxis: 'y',
    plugins: {
      tooltip: {
        callbacks: {
          label: function(context) {
            const descriptions = {
              'Openness': 'Curiosity, imagination, and preference for novelty.',
              'Conscientiousness': 'Organization, discipline, and reliability.',
              'Extraversion': 'Sociability, assertiveness, and energy.',
              'Agreeableness': 'Compassion, cooperation, and trust.',
              'Neuroticism': 'Emotional sensitivity and stress reactivity.'
            };
            return descriptions[context.label];
          }
        }
      }
    }
  }
});

// 16PF CHART
new Chart(document.getElementById('pf16-chart'), {
  type: 'bar',
  data: {
    labels: [
      'Warmth', 'Reasoning', 'Emotional Stability', 'Dominance',
      'Liveliness', 'Rule-Consciousness', 'Social Boldness', 'Sensitivity',
      'Vigilance', 'Abstractedness', 'Privateness', 'Apprehension',
      'Openness to Change', 'Self-Reliance', 'Perfectionism', 'Tension'
    ],
    datasets: [{
      label: 'Score',
      data: [4.2, 4.3, 4.2, 3.9, 3.3, 2.5, 3.4, 3.9, 2.2, 4.3, 1.4, 1.9, 4.7, 3.8, 2.5, 2.5],
      backgroundColor: '#ff6a8b'
    }]
  },
  options: {
    indexAxis: 'y',
    plugins: {
      tooltip: {
        callbacks: {
          label: function(context) {
            const descriptions = {
              'Warmth': 'Supportive, attentive, and friendly.',
              'Reasoning': 'Analytical thinking and problem-solving.',
              'Emotional Stability': 'Calmness and resilience.',
              'Dominance': 'Assertiveness and leadership.',
              'Liveliness': 'Spontaneity and enthusiasm.',
              'Rule-Consciousness': 'Respect for norms and structure.',
              'Social Boldness': 'Confidence in social situations.',
              'Sensitivity': 'Empathy and emotional awareness.',
              'Vigilance': 'Skepticism and cautiousness.',
              'Abstractedness': 'Imagination and introspection.',
              'Privateness': 'Discretion and guardedness.',
              'Apprehension': 'Self-doubt and worry.',
              'Openness to Change': 'Adaptability and curiosity.',
              'Self-Reliance': 'Independence and autonomy.',
              'Perfectionism': 'Organization and precision.',
              'Tension': 'Restlessness and urgency.'
            };
            return descriptions[context.label];
          }
        }
      }
    }
  }
});
</script>

<style>
.via-btn {
  background: #eee;
  border: none;
  padding: 8px 14px;
  margin: 6px 0;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9rem;
}
.via-btn:hover {
  background: #dcd3ff;
}
</style>

<style>
/* TAB WRAPPER */
.custom-tabs {
  display: block;
  margin-bottom: 1rem;
}

/* HIDE RADIO BUTTONS */
.custom-tabs input[type="radio"] {
  display: none;
}

/* TAB LABELS */
.custom-tabs label {
  display: inline-block;        /* ← THIS fixes the vertical stacking */
  padding: 10px 16px;
  margin-right: 4px;
  cursor: pointer;
  background: #2d2d2d;          /* dark background */
  color: #f0f0f0;               /* readable light text */
  border-radius: 6px 6px 0 0;
  font-weight: 600;
}

/* HOVER */
.custom-tabs label:hover {
  background: #444;
}

/* TAB CONTENT */
.tab-content {
  display: none;
  padding: 20px;
  background: #1e1e1e;          /* dark panel */
  color: #f0f0f0;               /* readable text */
  border: 1px solid #444;
  border-top: none;
  border-radius: 0 0 6px 6px;
}

/* ACTIVE TAB CONTENT */
#tab1:checked ~ #content1,
#tab2:checked ~ #content2,
#tab3:checked ~ #content3 {
  display: block;
}

/* ACTIVE TAB LABEL */
#tab1:checked + label,
#tab2:checked + label,
#tab3:checked + label {
  background: #ffffff;          /* active tab background */
  color: #000000;               /* readable active text */
  border-bottom: 1px solid #ffffff;
}
</style>
