# Hand Tracking with AI-Powered Problem Solving (Python + Streamlit)

This project integrates **real-time hand tracking** using **OpenCV** and **cvzone** with **Google's Generative AI model** (Gemini) to create an interactive drawing and problem-solving application. The interface is built using **Streamlit** to provide a seamless user experience.

---

## 🚀 **Features**

- Real-time hand tracking using webcam.
- Drawing on a virtual canvas with hand gestures.
- AI-powered problem solving by sending prompts to **Google's Gemini AI model**.
- Streamlit-based UI for live interaction and results display.

---

## 🛠️ **Tech Stack**

- **Python**
- **OpenCV**
- **cvzone** (Hand Tracking Module)
- **Google Generative AI (Gemini)**
- **Streamlit**
- **NumPy**
- **Pillow (PIL)**

---

## 📦 **Setup Instructions**

### 1️⃣ **Clone the Repository**
```bash
$ git clone https://github.com/yourusername/hand-tracking-ai.git
$ cd hand-tracking-ai
```

### 2️⃣ **Install Dependencies**
```bash
$ pip install -r requirements.txt
```

### 3️⃣ **Run the Application**
```bash
$ streamlit run app.py
```

---

## 🖐️ **Hand Gestures**
| Gesture          | Action                  |
|------------------|-------------------------|
| Index finger up  | Draw on the canvas      |
| All fingers up   | Clear the canvas        |
| Thumb down       | Send drawing to AI      |

---

## 📚 **File Structure**
```
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 🔑 **Google Generative AI API Setup**

To use the **Google Generative AI model**, configure the API key as follows:

1. Create an account on **Google Cloud** and enable the **Generative AI API**.
2. Obtain your API key.
3. Add the API key to your application:
   ```python
   genai.configure(api_key="YOUR_API_KEY")
   ```

---

## 🧪 **Dependencies**

- Python 3.7+
- OpenCV
- cvzone
- Streamlit
- NumPy
- Pillow
- google-generativeai

---

## 🤖 **How It Works**

1. **Hand Detection**: The application uses OpenCV and cvzone to detect hand gestures through the webcam.
2. **Drawing on Canvas**: Based on hand gestures, users can draw on a virtual canvas.
3. **AI Interaction**: When a specific gesture is detected (thumb down), the canvas drawing is sent to **Google's Generative AI** to solve or respond to a predefined prompt.

---

## 🌐 **Deployment**
You can deploy this application on any platform that supports **Streamlit**, such as **Streamlit Cloud**, **Heroku**, or **AWS**.

---

## 📋 **License**
This project is licensed under the **MIT License**. Feel free to use, modify, and distribute this project as you wish.

---

## 🤝 **Contributing**
Contributions are welcome! Feel free to open an **issue** or submit a **pull request** for any enhancements or bug fixes.

---

## 📞 **Contact**
- **Author**: Gautam Rahul
- **Email**: gautamrahul2003las@gmail.com
- **GitHub**: [https://github.com/gautam-rahul-09](https://github.com/gautam-rahul-09)







Happy coding! 😊

