# 🇵🇹 JurisPT

**JurisPT** is an open-source voice-to-text legal assistant built for residents of Portugal to query and understand laws affecting their daily lives — from housing rights to labor laws and data privacy. At its core, it leverages a **Retrieval-Augmented Generation (RAG)** architecture powered by real legislation from official government sources.

Built for transparency, customization, and accessibility.

---

## 🧠 Features

- 🔍 **Web scraping** of real legal documents from [Diário da República](https://dre.pt/)
- 🌍 **Multilingual support** (Portuguese 🇵🇹 + English 🇬🇧)
- 🧹 **Text preprocessing** — clean, normalize, and chunk legal text
- 🧠 **Semantic search** using vector embeddings
- 🗣️ **Voice-enabled** search via Whisper or Vosk
- 🧩 **Modular and hackable** — easily plug in more laws or swap models
- 🔁 **Incremental updates** — scrape and re-index new laws on demand
- 🐍 **Pythonic & production-ready** — built with maintainability in mind

---

## ⚙️ Why JurisPT?

- **Fully open-source**: inspect every layer, from crawling to UI
- **Customizable**: extend by adding new documents or switching vector DBs
- **No black box**: built entirely with transparent and modular components
- **Retrain? Not exactly.** Instead of retraining the model, we reindex updated documents using your embedder of choice — keeping it fast and efficient.

---

## 📁 Project Structure

```bash
JurisPT/
│
├── src/                       # root package
│   ├── legalscraper/          # gets laws documents from public sources
│   │   └── law_scraper.py
│   │
│   ├── processing/             # clean, normalize, chunk legal text
│   │   ├── cleaner.py
│   │   └── chunker.py
│   │
│   ├── vectorization/          # embed, store, and retrieve chunks
│   │   ├── embedder.py
│   │   ├── vectorstore.py
│   │   └── retriever.py
│   │
│   ├── ingestion/              # pipeline glue (scrape → clean → index)
│   │   ├── loader.py
│   │   └── pipeline.py
│   │
│   ├── prompts/                # prompt templates for QA
│   │   └── qa_prompt.txt
│   │
│   ├── api/                    # streamlit-based UI and logic
│   │   ├── main.py
│   │   └── ui_helpers.py
│   │
│   └── config.py               # central paths, constants, and ENV vars
│
├── corpus/                     # legal text and data from diário da república
│   ├── raw/                    # raw scraped text per law
│   ├── clean/                  # cleaned and chunked text for embedding
│   └── metadata/               # core index of laws to scrape
│
├── tests/                      # unit + integration tests
│   ├── test_scraper.py
│   ├── test_law_revoker.py
│   ├── test_cleaner.py
│   ├── test_chunker.py
│   ├── test_pipeline.py
│   └── test_api.py
│
├── cli.py                      # command-line tool for managing ingestion, scraping, etc
├── requirements.txt            # fallback for pip users
├── Dockerfile                  # containerized deploy
└── README.md
```

## 🚀 Getting Started

The easiest way to run JurisPT is via Docker.

### ▶️ Run with Docker

```bash
git clone https://github.com/dfranco-projects/JurisPT.git
cd JurisPT
docker build -t jurispt .
docker run -p 8501:8501 jurispt
```

> Access the app at [http://localhost:8501](http://localhost:8501)

### 🔧 Local Setup (Advanced)

If you prefer running things locally (dev mode):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
```

---

## 🧪 Example Usage

```bash
# scrape a specific law and reindex
python cli.py ingest --law-id=123/X/2023

# launch the Streamlit frontend
streamlit run src/api/main.py
```

---

## ⚙️ Environment Setup

No external API keys required — everything runs locally.

If needed, you can customize defaults (paths, model choice, etc.) in:

```bash
src/config.py
```

---

## 🔗 Data Sources

Legal documents are pulled directly from trusted government sources:

- [Diário da República](https://dre.pt/)
- [Portal da Justiça](https://justica.gov.pt/)
- [Portal da Habitação](https://www.portaldahabitacao.pt/)

---

## 🤝 Contributing

Have ideas to expand, optimize, or customize JurisPT? Open issues, submit PRs, or fork freely.

Legal professionals, civic tech hackers, and AI devs all welcome.
