# 🇵🇹 JurisPT

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
│
├── data/                        # Raw + processed law text files
│   ├── raw/                     # Raw HTML or scraped data
│   ├── clean/                   # Cleaned text chunks, paragraphs
│   └── metadata/                # Metadata about laws, e.g. law_dict.json
│       └── laws_metadata.json
│
├── scripts/                     # One-off scripts for scraping, cleaning, etc
│   ├── scrape_dre.py            # Scrape Diário da República using law_id
│   ├── clean_laws.py            # Strip HTML, normalize structure
│   ├── chunk_laws.py            # Split laws into chunks for RAG
│   └── ingest_to_vectorstore.py # Index into FAISS, ChromaDB, etc
│
├── retriever/                   # Vector store and retriever logic
│   ├── embedder.py              # SentenceTransformer or OpenAI embed logic
│   ├── vectorstore.py           # Vector DB handling
│   └── retriever.py             # Similarity + reranking logic
│
├── app/                         # UI or API interface
│   ├── main.py                  # CLI or Streamlit/FastAPI app
│   └── prompts/                 # Prompt templates for QA/generation
│       └── qa_prompt.txt
│
├── voice/                       # Optional: voice input → text interface
│   ├── speech_to_text.py        # Whisper or Vosk
│   └── mic_input.py             # Mic streaming logic
│
├── rag_pipeline/                # Full orchestration
│   ├── load.py                  # Load and preprocess sources
│   ├── build_index.py           # Embed + store docs
│   ├── query.py                 # RAG inference logic
│
├── tests/                       # Unit and integration tests
│
├── requirements.txt             # Python deps
└── README.md                    # Project intro
```

## 🚀 Getting Started
```bash
git clone git@github.com:dfranco-projects/JurisPT.git
cd JurisPT
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install

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
