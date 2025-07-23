# 👧🏼 Sara – Personal Multimodal AI Assistant

Sara is an intelligent, voice-controlled AI assistant powered by a **multimodal agent** that can think, speak, see, and respond based on user interactions. Designed for natural voice communication, Sara listens to your speech, understands your intent, and replies vocally — just like a human assistant.

---

## 🧠 Features

- 🎙️ **Voice Input & Output**: Talk to Sara using your voice. She listens and replies back — no typing needed.
- 🤖 **Multimodal AI Agent**: Built using **LangGraph**, the agent can reason whether it needs visual input (via webcam) or just provide a voice/text response.
- 💬 **Interactive Chat Window**: All conversations (your voice and Sara’s replies) are shown as text in the frontend chat.
- 📷 **Live Webcam Feed**: Integrated webcam stream using OpenCV, available directly in the Gradio interface.
- 🌐 **Frontend with Gradio**: Clean, responsive, and interactive interface for easy use.
- 🗣️ **Text-to-Speech with ElevenLabs**: Realistic voice responses powered by ElevenLabs API.
- 🎧 **Speech-to-Text using Whisper (via Groq)**: Transcribes your speech accurately using OpenAI’s Whisper model hosted via Groq.
- 🔌 **Extensible Architecture**: Designed to support future tools and integrations — expandable for custom workflows, external APIs, smart actions, and more.

---

## 🚀 Tech Stack

| Component        | Technology Used             |
| ---------------- | --------------------------- |
| Frontend         | Gradio                      |
| Webcam Access    | OpenCV                      |
| AI Agent         | LangGraph                   |
| Speech-to-Text   | OpenAI Whisper via Groq API |
| Text-to-Speech   | ElevenLabs                  |
| Audio Recording  | SpeechRecognition + PyDub   |
| Environment Vars | `python-dotenv`             |

---

## 🧠 How It Works

- Sara continuously listens in the background.

- When you speak, your voice is recorded and transcribed.

- The AI agent processes your query using LangGraph logic.

- It decides whether it needs visual input (from webcam) or not.

- Responds using ElevenLabs-generated voice.

- All interactions are shown in the Gradio chat window.

---

## 🧩 Future Plans

- Integrate tool calling (like calculators, web search, real-time weather, send and read email).

- Add memory and long-term context awareness.

- Plug in document/image understanding features.

---

## 🤝 Contributions

This is a personal but open-ended project. Feel free to contribute ideas, raise issues, or fork and experiment on your own version!

---

## ✨ Author

Aryan Gupta- [LinkedIn](https://www.linkedin.com/in/aryangupta2002/)
