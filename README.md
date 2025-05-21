# JurisPT

**JurisPT** is your voice-to-text legal assistant built for Portuguese residents to interact with everyday law - housing, labor rights, data protection, complaints, and more. It is built around Retrieval-Augmented Generation (RAG), using real legal documents from official Portuguese government sources.

## 🧠 Features
- Web scraping from Diário da República (Portugal's official gazette)
- Multilingual: works in both **Portuguese** and **English**
- Cleaned + chunked legal texts stored in a vector database
- Voice-to-text interface (optional)
- Query handling with retrieval + language model (RAG)
- Modular pipeline and retraining support

## 🗂️ Project Structure
```bash
JurisPT/
├── data/              # Raw, cleaned, and metadata law texts
├── scripts/           # Scraping, preprocessing, chunking, ingestion
├── retriever/         # Embedding and retrieval logic
├── rag_pipeline/      # End-to-end RAG orchestration
├── app/               # UI or CLI interface (FastAPI, Streamlit, etc)
├── voice/             # Speech recognition (Whisper, Vosk, etc)
├── tests/             # Unit and integration tests
```

## 🚀 Getting Started
```bash
git clone git@github.com:yourusername/JurisPT.git
cd JurisPT
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## ⚠️ Environment Variables
Create a `.env` file in the root directory with:
```
OPENAI_API_KEY=your_key_here
```

## 🔗 Data Sources
- [Diário da República](https://dre.pt/)
- [Portal da Justiça](https://justica.gov.pt/)
- [Portal da Habitação](https://www.portaldahabitacao.pt/)

## 🤝 Contributing
Open to collaboration. Reach out if you're passionate about AI + access to justice in Portugal.
