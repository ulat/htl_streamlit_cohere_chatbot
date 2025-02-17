from streamlit.testing.v1 import AppTest

PATH_TO_APP_MAIN_FILE = "../app.py"

UI_ELEMENT_KEYS = {
    "selectbox" : ["model"],
    "toggle": ["use_rag"],
    "button": ["clear_chat"],
    #"file_uploader": ["rag_docs"],
    "text_input": ["rag_url"],    
}
 
def test_cohere_api_key_label():
    at = AppTest.from_file(PATH_TO_APP_MAIN_FILE).run()
    assert at.text_input[0].label == "Introduce your Cohere API Key (https://dashboard.cohere.com/api-keys)"
   

def test_cochere_api_key_empty():
    at = AppTest.from_file(PATH_TO_APP_MAIN_FILE).run()
    at.text_input("cohere_api_key").set_value("").run()
    assert at.text_input("cohere_api_key").value == ""    
    assert at.warning[0].value.endswith("Please insert an API Key to continue...")

def all_sub_ui_elements_visible(at:AppTest, category:str) -> bool:
    for key in UI_ELEMENT_KEYS[category]:
        print(f"{category=}")
        match category:
            case "selectbox": 
                if not at.selectbox(key):            
                    return False
            case "toggle":
                if not at.toggle(key):            
                    return False
            case "button":
                if not at.button(key):            
                    return False
            case "file_uploader":
                if not at.file_uploader(key):            
                    return False
            case "text_input":
                if not at.text_input(key):            
                    return False
    return True

def all_ui_elements_visible(at:AppTest) -> bool:    
    for key in UI_ELEMENT_KEYS.keys():
        if not all_sub_ui_elements_visible(at, key):
            return False
    return True 
    
def test_render_elements_after_api_insert():
    at = AppTest.from_file(PATH_TO_APP_MAIN_FILE).run()
    at.text_input("cohere_api_key").set_value("1234567").run()    
    assert all_ui_elements_visible(at)
    
def test_enable_use_rag_toggle():
    """After adding a url to the rag-document store, we expect the use_rag toggle to be activated
    and the url added to the list of documents.
    """
    d
    assert at.toggle("use_rag").disabled    
    #assert not at.text_input("rag_url").disabled
    assert at.text_input("rag_url").placeholder == "https://example.com"    
    at.text_input("rag_url").set_value("https://htl-grieskirchen.at").run()    
    assert at.text_input("rag_url").value == "https://htl-grieskirchen.at"
    assert not at.toggle("use_rag").disabled    
    assert -1 != at.expander[0].label == "📚 Documents in DB (1)"
    
