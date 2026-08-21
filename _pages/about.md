---
layout: single
permalink: /about/
author_profile: true
title: "About Me"
header:
  image: "/assets/images/Portfolio_Banner.png"
classes: wide
---

{% include tabs.html %}

{% capture tab1 %}
## Big Five (OCEAN)

<div class="chart-container">
  <canvas id="big5-chart"></canvas>
</div>
{% endcapture %}

{% capture tab2 %}
## VIA Character Strengths

<div class="via-list">
  <ul>
    <li><button class="via-btn">Creativity</button></li>
    <li><button class="via-btn">Love of Learning</button></li>
    <li><button class="via-btn">Perspective</button></li>
    <li><button class="via-btn">Humor</button></li>
    <li><button class="via-btn">Leadership</button></li>
    <!-- Add more as needed -->
  </ul>
</div>
{% endcapture %}

{% capture tab3 %}
## 16PF

<div class="chart-container">
  <canvas id="pf16-chart"></canvas>
</div>
{% endcapture %}

{% include tabs.html
  tab1="Big Five"
  tab1content=tab1
  tab2="VIA Strengths"
  tab2content=tab2
  tab3="16PF"
  tab3content=tab3
%}

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
      backgroundColor: '#6a4cff',
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
    labels: ['Warmth', 'Reasoning', 'Emotional Stability', 'Dominance', 'Liveliness', 'Rule-Consciousness', 'Social Boldness', 'Sensitivity', 'Vigilance', 'Abstractedness', 'Privateness', 'Apprehension', 'Openness to Change', 'Self-Reliance', 'Perfectionism', 'Tension'],
    datasets: [{
      label: 'Score',
      data: [4.2, 4.3, 4.2, 3.9, 3.3, 2.5, 3.4, 3.9, 2.2, 4.3, 1.4, 1.9, 4.7, 3.8, 2.5, 2.5],
      backgroundColor: '#ff6a8b',
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
