from browser import document, ajax, html
from browser.local_storage import storage
import json, re

def search(event):
    caste = document['caste'].value
    religion = document['religion'].value
    converted_value = document['converted'].value
    key = f"{caste}-{religion}-{converted_value}"
    data = {
        'caste': caste,
        'religion': religion,
        'converted': converted_value
    }
    if converted_value:
        data['converted'] = converted_value == 'true'
    print(data)
    def on_complete(req):
        if req.status == 200:
            response = json.loads(req.text)
            storage[key] = f"{response}"
            if response == 'None':
                ajax.post('/posts/scholarships/', data=json.dumps(data), headers={'Content-Type': 'application/json'}, oncomplete=on_complete)
            sections = re.split(r'(<h1>.*?</h1>)', response)

# Merging title with its corresponding content
            sections = [sections[i] + sections[i+1] for i in range(1, len(sections)-1, 2)]
            res = document['ai-response']
            res.html = ""
            for idx, section in enumerate(sections):
                div = html.DIV()
                div.innerHTML = section
                res <= div
        else:
            document['ai-response'].innerHTML = f'Error: {req.status} - {req.text}'
    
    if storage.get(key) is not None :
        result = storage[key]
        if result == 'None':
            del storage[key]
            ajax.post('/posts/scholarships/', data=json.dumps(data), headers={'Content-Type': 'application/json'}, oncomplete=on_complete)
        else:
            print(result)
            sections = re.split(r'(<h1>.*?</h1>)', result)

# Merging title with its corresponding content
            
            sections = [sections[i] + sections[i+1] for i in range(1, len(sections)-1, 2)]
            res = document['ai-response']
            res.html = ""
            for idx, section in enumerate(sections):
                div = html.DIV()
                div.innerHTML = section
                res <= div
    else:
        ajax.post('/posts/scholarships/', data=json.dumps(data), headers={'Content-Type': 'application/json'}, oncomplete=on_complete)

document['search'].bind('click', search)
