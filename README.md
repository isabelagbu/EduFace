## Project Info
#### # ====================================
#### # App Name: Eduface
#### # Description: Eduface - Educational Facial Analysis for Cognitive Engagement
#### # Authors:
- **Isabel Agbu**
  - ID: 300378791
  - Email:agbui@student.douglascollege.ca
- **Nathan Bussabok**
  - ID: 300375256
  - Email: bussabokn@student.douglascollege.ca
- **William Delmanto**
  - ID: 300375603  
  - Email: rodriguesdelmaw@student.douglascollege.ca
#### # ====================================

# Emotion-Triggered Micro-Adaptation (EduFace)
*A real-time adaptive learning system using webcam emotion detection.*

This project implements a **video-based, emotion-aware learning system** that detects learner emotions through a webcam and triggers **micro-adaptations** (quizzes, summaries, pauses, encouragement messages) to improve engagement and comprehension.  
Developed as part of the research paper:

**“Emotion-Triggered Micro-Adaptation: A Real-Time Feedback System for Personalized Digital Learning”**  
*Douglas College, 2025*

<p align="center">
<img width="460" height="271" alt="image" src="https://github.com/user-attachments/assets/82ed309a-1d42-46c2-a885-fd198facae1a" style="width: 850px; height:530px"/>
</p>

Research Questions:
1. Which learner emotions can be reliable detected in real time using facial expressions during learning sessions?
2. How can real-time emotion detection be used to trigger adaptive micro-interventions (e.g., pauses, hints, content speed changes) during content delivery?
3. To what extent does real-time emotion-aware improve learner engagement and immediate content comprehension compared to non-adaptive systems?

Research Objectives:
1. To assess the real-time detection accuracy of learner emotions based on facial expressions during digital learning.
2. To design and implement adaptive micro-inventions (e.g., pauses, content slowing, hints) based on real-time emotional cues.
3. To evaluate the impact on emotion-triggered real-time adaptations on learner engagement and short-term comprehension.

--- 

## Key Features

- **Webcam Emotion Detection** using DeepFace + OpenCV  
- **Real-Time Adaptations**, including:  
  - Recall questions  
  - Summaries  
  - Encouragement messages  
  - Rewind  
  - Slow playback  
  - Pause & reflect  
- **Socket.IO communication** between frontend and backend  
- **React + TypeScript video-based learning UI**  
- **Adaptation logs** for research and analysis

--- 

## Research Results (Pilot Study)

- Tested with **12 Douglas College students**  
- **82 micro-adaptations** triggered across sessions  
- **Question recaps** identified as the most effective intervention  
- Participants reported higher focus vs. traditional video learning  
- Average quiz score: **6.75 / 10**  
- Strong interest in using similar systems for studying challenging material  

--- 

## Tech Stack

**Frontend:** React, TypeScript, Socket.IO  
**Backend:** Python, DeepFace, OpenCV, Socket.IO Server  

---

## How It Works

1. Webcam frames are captured and sent to the backend via sockets  
2. DeepFace analyzes the dominant emotion  
3. Emotion → pedagogical state mapping determines:  
   - Engagement  
   - Disengagement  
   - Confusion  
   - Frustration  
4. The system triggers a micro-adaptation using thresholds + cooldown timers  
5. Events are logged for later analysis

<img width="380" height="277" alt="image" src="https://github.com/user-attachments/assets/5953a9bf-05de-48f2-8a91-1af25dccde9e" />

## Initial Setup (Windows)
To start developing this wonderful idea, you need to follow these steps:

1. Download and install
- [Python 3.12](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/download)
- [GitHub Desktop](https://desktop.github.com/)
2. Clone the existing repository

### Setting up Frontend (Windows)
1. Open Command Prompt (cmd) as administrator
2. Navigate to your project directory:
   ```
   cd path\to\EduFace\Frontend
   ```
3. Install the required packages:
   ```
   npm install
   ```

## Usage
### Running the Frontend
4. Run the main script:
   ```
   npm run dev
   ```

### Setting up Backend (Windows)
1. Open Command Prompt (cmd) as administrator
2. Navigate to your project directory:
   ```
   cd path\to\EduFace\Backend
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
### Running the Backend
4. Run the main script:
   ```
   python .\main.py
   ```
