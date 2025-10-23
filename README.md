# 🧠 Anatomy & Physiology Flashcard Quiz App

An interactive desktop application built with Python and PySimpleGUI to help students master **Anatomy and Physiology I & II**. Quiz yourself on organs, bones, muscles, and body systems with real-time performance tracking.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ✨ Features

- 🎯 **Interactive GUI** – Clean, user-friendly interface built with PySimpleGUI
- 📚 **CSV-Based Flashcards** – Easy to edit and expand your question bank
- 🔀 **Randomized Questions** – Different quiz experience every session
- 📊 **Performance Tracking** – Monitor correct/incorrect answers and accuracy
- 💯 **Final Score Display** – See your results and track improvement
- 📴 **Fully Offline** – No internet connection required
- 🔧 **Expandable** – Simply add more questions to the CSV file

---

## 📂 Project Structure


anatomy_flashcards/
│
├── flashcards.csv       # Anatomy & physiology flashcard database
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── setup_env.sh         # Setup script for macOS/Linux
├── setup_env.bat        # Setup script for Windows
└── README.md           


---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or newer
- pip (Python package installer)

### Installation

1. **Clone the repository**
   
   git clone https://github.com/<your-username>/anatomy-flashcards.git
   cd anatomy-flashcards
   

2. **Install dependencies**
   
   pip install -r requirements.txt
   

   Or use the automated setup scripts:
   
   **macOS/Linux:**
   
   bash setup_env.sh
   
   
   **Windows:**
   
   setup_env.bat
   

3. **Run the application**

   python main.py
   

---

## 📖 How to Use

1. Launch the app with `python main.py`
2. A flashcard question will appear on screen
3. Type your answer in the input field
4. Click **Submit** to check if you're correct
5. Continue through all questions
6. View your final score and accuracy percentage

---

## 📝 Flashcard Format

The app reads from `flashcards.csv`, which should follow this format:

Question,Answer
What is the largest bone in the human body?,Femur
Which organ produces insulin?,Pancreas
What is the basic unit of life?,Cell
Name the three types of muscle tissue,Skeletal cardiac smooth


**Tips for adding flashcards:**
- Keep answers concise and consistent
- Use lowercase for easier matching (if applicable)
- Ensure proper CSV formatting with no extra commas

---

## 🛠️ Dependencies


PySimpleGUI
pandas


Install all dependencies with:

pip install -r requirements.txt


---

## 🔧 Customization Ideas

Want to extend the app? Here are some ideas:

- ⏱️ Add a timer mode for timed practice
- 🏷️ Implement category filtering (bones, muscles, organs, etc.)
- 💾 Save scores to a database or JSON file
- 🎲 Create a multiple-choice mode
- 📈 Add progress graphs and statistics
- 🎨 Customize themes and colors

---

## ❗ Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'PySimpleGUI'` | Run `pip install -r requirements.txt` |
| GUI window doesn't appear | Verify Python 3.8+ is installed: `python --version` |
| CSV file not loading | Check that `flashcards.csv` exists and has proper headers |
| App closes immediately | Run from terminal/command prompt to see error messages |
| Encoding errors | Ensure CSV is saved in UTF-8 encoding |

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork this repository
2. Create a new branch (`git checkout -b feature/new-flashcards`)
3. Add flashcards or improve functionality
4. Commit your changes (`git commit -m 'Add 50 new bone flashcards'`)
5. Push to the branch (`git push origin feature/new-flashcards`)
6. Open a Pull Request

**Especially helpful:**
- Adding more anatomy & physiology questions
- Improving the GUI design
- Bug fixes and performance improvements

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use, modify, and distribute for educational purposes.

---

## 👨‍💻 Author

**Giuliano Ercole**  
📍 Tampa, FL  
🎓 Nursing Student & InfoSec Specialist

Connect with me:
- GitHub: [@GiulianoErcole](https://github.com/GiulianoErcole)
- LinkedIn: [Your Profile](https://www.linkedin.com/in/giuliano-ercol%C3%A9-p)

---

## 🌟 Support This Project

If you find this app helpful for your studies:
- ⭐ Star this repository
- 🔄 Share it with classmates

**Happy studying! 📚💪**
