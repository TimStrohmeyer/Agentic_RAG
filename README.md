# Agentic RAG
This is a test architecture for an agentic RAG pipeline.

This QA Tool should be able to answer:
- **wiki questions**: Descriptive questions or questions regarding naming conventions, technical terms and process descriptions
  <br> (database: wiki entries, Naming Conventions, Business Glossary, Data Catalogue)
- **data lineage questions**: Questions regarding source systems of different data. NOTE: requires sql prompting
  <br> (database: sql database + Data catalogue)

**Architecture Diagram**:
![LLM Chatbot - Diagram](https://github.com/TimStrohmeyer/Agentic_RAG/assets/133879815/2d549a8c-f3b7-48dc-b921-7d20bc4c13bc)

Run app:
```
streamlit run streamlit_app.py 
