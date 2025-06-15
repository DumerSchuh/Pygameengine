import os
import json
import hashlib
import base64
base_dir=os.path.dirname(os.path.abspath(__file__))
def clear():
    os.system('cls')
def enter():
    input("")
def enterclear():
    enter()
    clear()
def _key_stream(schluessel, laenge):
    stream = b''
    counter = 0
    while len(stream) < laenge:
        data = f"{schluessel}{counter}".encode('utf-8')
        stream += hashlib.sha256(data).digest()
        counter += 1
    return stream[:laenge]
def hashen(txt,key):
    text_bytes = txt.encode('utf-8')
    key_bytes = _key_stream(key, len(text_bytes))
    encoded = bytes([b ^ k for b, k in zip(text_bytes, key_bytes)])
    return base64.b64encode(encoded).decode('utf-8')
def hashde(text,key):
    encoded = base64.b64decode(text)
    key_bytes = _key_stream(key, len(encoded))
    decoded = bytes([b ^ k for b, k in zip(encoded, key_bytes)])
    return decoded.decode('utf-8')
def loadlang(langsel):
    global lang
    lang_path=os.path.join(base_dir,"..\\lang",f"{langsel}.json")
    with open(lang_path,"rt",encoding="utf-8") as f:
        return json.load(f)
def loadsettings():
    settings_path=os.path.join(base_dir,"..","settings.json")
    with open(settings_path,"rt",encoding="utf-8") as f:
        return json.load(f)
def loadsellang():
    try:
        __path=os.path.join(base_dir,"..\\accounts","sellang.json")
        with open(__path,"rt",encoding="utf-8") as f:
            langsel1=json.load(f)
            return langsel1["selectlang"]
    except:
        return "en"