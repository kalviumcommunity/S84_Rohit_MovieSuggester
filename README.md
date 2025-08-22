# 🎬 AI Movie Suggester with RAG + Gemini LLM

## 📌 Project Idea
The AI Movie Suggester is an intelligent system that recommends movies based on user preferences such as genre, actors, directors, or mood.  
It uses **RAG (Retrieval-Augmented Generation)** to fetch relevant information from a movie dataset and **Google Gemini LLM** to generate natural language responses.

For example:
- User: *"Suggest me a sci-fi movie with time travel."*  
- AI: *"I recommend 'Interstellar' (2014) — directed by Christopher Nolan. It’s a mind-bending sci-fi film with themes of time dilation and survival."*

---

## ⚙️ Implementation
1. **Dataset**: Movie metadata (genres, actors, directors, plot summaries).  
2. **RAG Pipeline**:  
   - Retrieve relevant movies from dataset based on user query.  
   - Use Gemini LLM to refine and generate human-like recommendations.  
3. **LLM Features**:  
   - Zero-shot, one-shot, and few-shot prompting.  
   - Dynamic prompting (based on user context).  
   - Custom temperature & token control for creativity vs. accuracy.  

---

## 🛠️ Tech Stack
- **Google Gemini API** (LLM for natural language recommendations).  
- **LangChain** (for RAG + prompt orchestration).  
- **MovieLens Dataset / Custom Movie Dataset** (for retrieval).  
- **Python** (backend).  

---

## 📚 Assignments Covered
This project includes the following AI/LLM concepts:
1. System & User Prompts  
2. Zero-Shot Prompting  
3. One-Shot Prompting  
4. Multi-Shot Prompting  
5. Dynamic Prompting  
6. Chain of Thought Prompting  
7. Tokens & Tokenization  
8. Temperature  
9. Top P Sampling  
10. Create Project Readme  

---

## 🎥 Video Explanation
In the video:
- I’ll explain the project idea.  
- Show how RAG + Gemini is used.  
- Walk through each assignment implementation.  

---

## 🚀 Future Work
- Add embeddings & vector database (Pinecone / FAISS).  
- Implement cosine similarity & L2 similarity.  
- Build a frontend UI for users to interact.  
