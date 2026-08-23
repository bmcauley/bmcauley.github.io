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
  <label for="tab2">VIA</label>

  <input type="radio" id="tab3" name="tabs">
  <label for="tab3">16PF</label>

  <div class="tab-content" id="content1">
    <h3>Big Five (OCEAN) Model</h3>
    <canvas id="big5-chart"></canvas>

  <div class="notice--info">
    Curious about this assessment?  
    <a href="/about/big5">Learn more here.</a>
  </div>
  </div>

<style>
#content2 p {
  font-size: 0.75rem !important;
  line-height: 1.3;
}

#content2 p i {
  font-size: 0.75rem !important;
}
</style>

  <div class="tab-content" id="content2">
    <h3>VIA Character Strengths (Top 5)</h3>
      <button class="via-btn"><i class="fa-solid fa-palette"></i> Creativity</button>
      <p>
        <i>"I am creative, conceptualizing something useful, coming up with ideas that result in something worthwhile."</i>
      </p>

   <button class="via-btn"><i class="fa-solid fa-graduation-cap"></i> Love of Learning</button>
      <p>
        <i>"I am motivated to acquire new levels of knowledge, or deepen my existing knowledge or skills in a significant way."</i>
      </p>
  
   <button class="via-btn"><i class="fa-solid fa-comment-medical"></i> Perspective</button>
      <p>
        <i>"I give advice to others by considering different (and relevant) perspectives and using my own experiences and knowledge to clarify the big picture."</i>
      </p>

     <button class="via-btn"><i class="fa-solid fa-face-laugh-beam"></i> Humor</button>
      <p>
        <i>"I approach life playfully, making others laugh, and finding humor in difficult and stressful times."</i>
      </p>

     <button class="via-btn"><i class="fa-solid fa-heart-circle-check"></i> Leadership</button>
      <p>
        <i>"I take charge and guide groups to meaningful goals, and ensure good relations among group members."</i>
      </p>

  <div class="notice--info">
    Descriptions provided by VIA Institute. Curious about this assessment?  
    <a href="https://www.viacharacter.org/">Discover your strengths here!</a>
  </div>
  </div>

  <div class="tab-content" id="content3">
    <h3>Cattell's 16 Personality Factors</h3>
    <canvas id="pf16-chart"></canvas>
  </div>

</div>


<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2"></script>

<script>
// REGISTER PLUGIN
Chart.register(ChartDataLabels);

new Chart(document.getElementById('big5-chart'), {
  type: 'bar',
  data: {
    labels: ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism'],
    datasets: [{
      label: 'Score',
      data: [99, 61, 38, 74, 14],
      backgroundColor: '#5e4cff',
      barPercentage: 0.9,
      categoryPercentage: 0.8
    }]
  },
  options: {
    indexAxis: 'y',
    scales: {
      y: {
        ticks: {
          color: '#1e1e1e',
          font: { size: 16, weight: '400' }
        }
      },
      x: {
        ticks: {
          color: '#1e1e1e',
          font: { size: 14 }
        }
      }
    },
    plugins: {
      legend: { display: false },
      datalabels: {
        color: '#1e1e1e',
        anchor: 'end',
        align: 'right',
        font: { size: 14, weight: '600' },
        formatter: value => value
      },
      tooltip: {
        callbacks: {
          label: function(context) {
            const descriptions = {
              'Openness': 'Degree to which a person is creative, imaginative, and prefers novelty.',
              'Conscientiousness': 'Tendency to be responsible, organized, and self-disciplined',
              'Extraversion': 'Degree to which a person feels energized by social/external activity.',
              'Agreeableness': 'Tendency to be cooperative, trusting, and prioritizing social harmony.',
              'Neuroticism': 'Tendency to experience negative emotions in response to stress or uncertainty.'
            };
            return descriptions[context.label];
          }
        }
      }
    }
  }
});

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
      backgroundColor: '#5e4cff',
      barThickness: 24
    }]
  },
  options: {
    indexAxis: 'y',
    scales: {
      y: {
        ticks: {
          color: '#1e1e1e',
          font: { size: 16, weight: '400' }
        }
      },
      x: {
        ticks: {
          color: '#1e1e1e',
          font: { size: 14 }
        }
      }
    },
    plugins: {
      legend: { display: false },

      datalabels: {
        color: '#1e1e1e',
        anchor: 'end',
        align: 'right',
        font: { size: 14, weight: '600' },
        formatter: value => value
      },

      tooltip: {
        callbacks: {
          label: function(context) {
            const descriptions = {
              'Warmth':'Low - Reserved | High - Outgoing',
              'Reasoning': 'Low - Concrete | High - Abstract',
              'Emotional Stability': 'Low - Reactive | High - Calm',
              'Dominance': 'Low - Accommodating | High - Assertive',
              'Liveliness': 'Low - Serious | High - Lively',
              'Rule-Consciousness': 'Low - Expedient | High - Conscientious',
              'Social Boldness': 'Low - Shy | High - Confident',
              'Sensitivity': 'Low - Objective | High - Empathetic',
              'Vigilance': 'Low - Trusting | High - Skeptical',
              'Abstractedness': 'Low - Grounded | High - Imaginative',
              'Privateness': 'Low - Forthright | High - Discreet',
              'Apprehension': 'Low - Self-assured | High - Self-doubting',
              'Openness to Change': 'Low - Traditional | High - Progressive',
              'Self-Reliance': 'Low - Group-oriented | High - Independent',
              'Perfectionism': 'Low - Flexible | High - Organized',
              'Tension': 'Low - Relaxed | High - Tense'
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
  background: #2d2d2d;
  color: #fff;
  border: none;
  padding: 8px 14px;
  margin: 6px 0;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9rem;
}
.via-btn:hover {
  background: #5e4cff;
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
  background: #f0f0f0;          /* dark panel */
  color: #1e1e1e;               /* readable text */
  border: 1px solid #959595;
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
  background: #5e4cff;          /* active tab background */
  color: #ffffff;               /* readable active text */
  /* border-bottom: 1px solid #ffffff;*/
}
</style>
