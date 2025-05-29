# 🇵🇹 JurisPT (WIP)

**JurisPT** is an open-source legal assistant built for Portugal. It helps users **understand laws**, **write juridical-style texts** (like formal emails or resignation letters), and **navigate small legal problems**—from housing issues to labor rights. All without relying on external services.

JurisPT runs entirely on your machine. No hidden APIs. No internet dependency. Fully transparent and under your control.

---

## 🧠 What JurisPT Does

* **Download** legal texts from [Diário da República](https://diariodarepublica.pt/dr/home) automatically  
* **Support** inquiries in Portuguese 🇵🇹 and English 🇬🇧  
* **Clean and split** long documents for fast, reliable search  
* **Semantic search** using advanced text embeddings  
* **Spoken queries**: ask questions by speaking (all processing is local)  
* **Modular design**: easily add new laws, swap models, or extend features  
* **Keep content fresh**: re-scrape and re-index updated laws anytime  

---

## 🛠️ Technology Stack

* **Python 3.12+**
* **Playwright** – fast, reliable scraping
* **Streamlit** – intuitive web interface for users
* **tiktoken** – efficient text tokenization
* **Sentence Transformers** – high-quality local text embeddings
* **FAISS** – fast, local vector search for semantic retrieval
* **Pandas** – robust data handling and transformation
* **spaCy** – named-entity recognition and text preprocessing
* **LangChain** – orchestration of the RAG pipeline, prompt routing, and tool usage
* **Hugging Face Transformers** – local LLM access and fine-tuning
* **Whisper** – offline speech-to-text for spoken legal queries
* **Pytest** – unit and integration testing
* **Docker** – reproducible environments and deployment


> All processing and search happen locally—no external services needed.

---

## ⚡ Why Choose JurisPT

* **Open source:** review and modify every part  
* **Customizable:** plug in new data sources or tools  
* **Transparent:** no hidden logic or vendor lock-in  
* **Efficient updates:** refresh the index instead of retraining  

---

## 📁 Project Layout

```bash
JurisPT/
├── src/
│   ├── legalscraper/    # download and parse laws
│   ├── processing/      # clean and split text
│   ├── vectorization/   # embed text and search
│   ├── ingestion/       # pipeline orchestration
│   ├── prompts/         # prompt templates for queries
│   ├── api/             # Streamlit app files
│   └── config.py        # configuration settings
├── corpus/              # raw and processed legal texts
├── tests/               # unit and integration tests
├── cli.py               # command-line interface
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker build instructions
└── README.md            # this file
```

---

## 🚀 Quick Start

### 1. Run with Docker

```bash
git clone https://github.com/dfranco-projects/JurisPT.git
cd JurisPT
docker build -t jurispt .
docker run -p 8501:8501 jurispt
```

Access the web app at [http://localhost:8501](http://localhost:8501)

### 2. Local Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
```

---

## 🧪 Example Commands

```bash
# Download and reindex a law:
python cli.py ingest --law-id=123/X/2023

# Start the web interface:
streamlit run src/api/main.py
```

---

## 🔗 Data Source

* Diário da República: [https://diariodarepublica.pt/dr/home](https://diariodarepublica.pt/dr/home)

---

## 🤝 Contributing

Contributions are welcome! Open issues, submit pull requests, or fork the repo.

Legal experts, civic tech enthusiasts, and AI developers: let’s build together.