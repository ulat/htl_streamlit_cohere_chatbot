# LLM Chatbot App

RAG web application using Python, Streamlit and LangChain, so you can chat with Documents, Websites and other custom data.

## To run streamlit-app locally:

```bash
$ git clone <this-repo-url>

$ cd <this-repo-folder>

$ python -m venv venv

$ venv\Scripts\activate  # or source venv/bin/activate in Linux/Mac

$ pip install -r requirements.txt

$ streamlit run src/app.py
```

## To run the UI-tests locally:

```bash
$ pytest src/tests 
```

## Slide Show

To run the slideshow from the [`rag_chatbot_basics.ipynb`](rag_chatbot_basics.ipynb) file you can just open the html-file: [rag_chatbot_basics.html.ipynb](rag_chatbot_basics.html.ipynb)

To generate the slide yourself, use the followind commands within a terminal:

First clone the reveal.js into your project folder:

```bash
git clone https://github.com/hakimel/reveal.js.git
```

Then create the reveal.js HTML slideshow:

```bash
// on mac you have to export the jupyter path:
// $ export JUPYTER_PATH=/opt/homebrew/share/jupyter:$JUPYTER_PATH
nbconvert rag_chatbot_basics.ipynb --to slides --reveal-prefix reveal.js
```

To host the slideshow directly in the browser use the `--post serve` parameter:

```bash
nbconvert rag_chatbot_basics.ipynb --to slides --reveal-prefix reveal.js --post serve
```