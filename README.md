# Janesh-Assignment
# Persona-Adaptive Customer Support Agent

## Project Overview

This project is an AI-powered customer support agent that automatically detects customer personas, retrieves relevant information from a knowledge base using Retrieval-Augmented Generation (RAG), generates persona-specific responses, and escalates unresolved issues to a human support representative.

Supported Personas:

* Technical Expert
* Frustrated User
* Business Executive

---

## Features

* Persona Detection
* RAG-based Knowledge Retrieval
* Adaptive Response Generation
* Human Escalation Workflow
* Human Handoff Summary
* Streamlit Web Interface

---

## Tech Stack

| Component       | Technology              |
| --------------- | ----------------------- |
| Language        | Python 3.11             |
| UI              | Streamlit               |
| LLM             | Google Gemini 1.5 Flash |
| Embeddings      | Sentence Transformers   |
| Vector Database | FAISS                   |
| Framework       | LangChain               |
| Document Loader | PyPDF                   |

---

## Architecture

User Query
→ Persona Detection
→ Knowledge Retrieval (RAG)
→ Response Generation
→ Escalation Check
→ Human Handoff Summary

---

## Persona Detection Strategy

The system identifies customer personas using keyword analysis and prompt-based classification.

### Technical Expert

Characteristics:

* Uses technical terminology
* Requests logs or configurations
* Wants detailed explanations

### Frustrated User

Characteristics:

* Uses emotional language
* Expresses dissatisfaction
* Requests urgent help

### Business Executive

Characteristics:

* Outcome-focused
* Interested in business impact
* Prefers concise communication

---

## RAG Pipeline Design

1. Load support documents from the docs directory.
2. Split documents into chunks.
3. Generate embeddings using Sentence Transformers.
4. Store embeddings in FAISS.
5. Retrieve top-k relevant chunks for user queries.
6. Pass retrieved context to Gemini for grounded response generation.

### Chunking Strategy

* Chunk Size: 500
* Chunk Overlap: 50

### Retrieval Strategy

* Similarity Search
* Top-k = 3

---

## Escalation Logic

The conversation is escalated when:

* No relevant information is found
* Retrieval confidence is below threshold
* User remains dissatisfied
* Billing, legal, or account-sensitive issues occur

Confidence Threshold:

* 0.30

---

## Setup Instructions

### Clone Repository

git clone <repository-url>

cd persona-support-agent

### Create Virtual Environment

python -m venv venv

### Activate Environment

Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

### Install Dependencies

pip install -r requirements.txt

### Add Environment Variables

Create a .env file:

GEMINI_API_KEY=your_api_key

### Run Application

streamlit run app.py

---

## Environment Variables

| Variable       | Description    |
| -------------- | -------------- |
| GEMINI_API_KEY | Gemini API Key |

---

## Example Queries

### Technical Expert

Can you explain API authentication failure and provide error details?

### Frustrated User

I have tried everything and nothing works!

### Business Executive

How does this issue impact operations and when will it be resolved?

### Password Reset

Unable to reset my password.

### Escalation Example

My account has been suspended and I need legal clarification.

---

## Knowledge Base

The knowledge base contains customer support articles, FAQs, troubleshooting guides, billing policies, and account management documents used for retrieval.

---

## Known Limitations

* Limited to the available knowledge base documents.
* Keyword-based persona detection may misclassify edge cases.
* Retrieval quality depends on document quality.
* Human escalation is rule-based.

---

## Future Improvements

* Multi-turn conversation memory
* LangGraph workflow
* Sentiment analysis
* Feedback collection
* Confidence scoring dashboard

---

## Demo

### GitHub Repository

<GitHub Link>

### Streamlit Application

<Streamlit Link>

### Screen Recording

<Drive/Loom Link>
