# Do your LLM even RAG bro?

RAG web application using Python, Streamlit and LangChain, so you can chat with Documents, Websites and other custom data.

To run it locally:

```bash
$ git clone <this-repo-url>

$ cd <this-repo-folder>

$ python -m venv venv

$ venv\Scripts\activate  # or source venv/bin/activate in Linux/Mac

$ pip install -r requirements.txt

$ streamlit run src/app.py
```

To run the UI-tests locally:

```
$ pytest src/tests 
```