# 🧠 Career & Learning Path Predictor  

[![Built with Jaseci](https://img.shields.io/badge/Built%20with-Jaseci-blueviolet?style=for-the-badge)](https://jaseci.org)
[![Powered by Gemini 2.0 Flash](https://img.shields.io/badge/Powered%20by-Gemini%202.0%20Flash-blue?style=for-the-badge)](https://deepmind.google/technologies/gemini/)
[![AI Project](https://img.shields.io/badge/Category-AI%20%7C%20Machine%20Learning-orange?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)]()

---

### Overview  
The **Career & Learning Path Predictor** is an intelligent agent built using **Jaseci** and powered by **Gemini 2.0 Flash**, a cutting-edge large language model.  
It analyzes a user’s **skills, interests, and personality** to recommend fitting career paths and tailored learning directions.  

This project highlights how **AI-driven reasoning** and **semantic modeling** can be applied to real-world decision support — from career guidance to personal growth.

---

## Features  

**Profile Modeling** – Captures a person’s background, skills, and personality traits.  
**Career Suggestion** – Suggests suitable career paths aligned with the user’s abilities.  
**Learning Path Generator** – Recommends next steps such as courses, tools, or technologies to learn.  
**LLM Integration** – Uses `byllm` with the **Gemini 2.0 Flash** model for intelligent reasoning.  
**Single-File Simplicity** – Entire logic is contained in one `.jac` file (`predictor.jac`).  

---

## How It Works  

1. **Profile Creation**  
   The `Profile` object defines a user’s background and context:
   ```jac
   obj Profile {
       has name: str;
       has age: int;
       has interests: list[str];
       has skills: list[str];
       has personality_type: list[str];
   }
   ```

2. **Career Prediction**  
   ```jac
   def suggest_career(profile: Profile) -> list[str] by llm();
   ```
   Uses Gemini to propose the most suitable career options based on the profile.

3. **Learning Path Recommendation**  
   ```jac
   def learning_path(profile: Profile, chosen_career: str) -> str by llm();
   ```
   Suggests a personalized roadmap — what skills, tools, or courses to pursue next.

4. **Walker Execution**  
   A test walker runs the process by:
   - Creating a demo user (e.g., *Nelly Mogere, 22, AI & Cybersecurity enthusiast*).  
   - Asking the model for career suggestions.  
   - Printing the top career and an AI-generated learning path.

---

## Example Output  
```
Focused career: AI Researcher

Recommended learning path:
Start by mastering Python and TensorFlow for deep learning, then explore MLOps, cloud tools, and large-scale data handling.
```

---

## Getting Started  

### 1️⃣ Create & Activate a Virtual Environment  
```bash
python -m venv jac-env
jac-env\Scripts\activate     # Windows
```

### 2️⃣ Install Jaseci  
```bash
pip install jaseci
```

### 3️⃣ Run the Predictor  
Make sure you are in the same directory as `predictor.jac`, then execute:  
```bash
jac run predictor.jac
```

---

##  Applications  
- Career and student counseling platforms  
- Personalized education advisors  
- Mentorship or talent development tools  
- Self-assessment and learning recommendation systems  

---

## Author  
**Nelly Gesare Mogere**  
 AI & Cybersecurity Enthusiast | Software Developer | Machine Learning Explorer  
 *Chuka University, Kenya*  

---
