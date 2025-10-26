function finishQuiz(){
  const values = [];
  sliders.forEach(slider => values.push(parseInt(slider.value)));
  slides.forEach(slide => slide.classList.remove('active'));
  document.getElementById('progressBar').style.width = '100%';

  const categories = {
    Relationships: (values[0] + values[5]) / 2,
    Discipline: (values[1] + values[8]) / 2,
    Adaptability: (values[2] + values[4]) / 2,
    SelfAwareness: (values[3] + values[9]) / 2,
    Curiosity: values[6],
    Teamwork: values[7]
  };

  const avg = values.reduce((a,b)=>a+b,0) / values.length;
  let feedback = '';
  if(avg >= 4)
    feedback = "🌟 You exhibit strong emotional intelligence, adaptability, and purpose-driven focus — a true growth-oriented individual.";
  else if(avg >= 2.5)
    feedback = "🌈 You possess balanced traits and self-awareness. Keep nurturing consistency and personal reflection.";
  else
    feedback = "💭 You show introspective tendencies — explore new experiences and build confidence through gradual challenges.";

  // Save quiz results to localStorage before redirecting
  localStorage.setItem("quizResults", JSON.stringify({
    categories,
    avg,
    feedback
  }));

  // Tell user briefly then redirect to login
  document.getElementById('result').innerHTML = `
    <h2>Saving your results...</h2>
    <p>Redirecting you to login page. Please wait...</p>
  `;
  document.getElementById('feedback').innerHTML = "";

  setTimeout(() => {
    window.location.href = "https://daac2ac1-4b56-4262-83f6-278908cbbd50-00-3vmla8q63ds8f.janeway.replit.dev/";
  }, 2000);
}
