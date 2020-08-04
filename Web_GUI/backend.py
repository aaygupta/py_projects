import eel, os
from googletrans import Translator

path = os.path.dirname(os.path.realpath(__file__))
web_folder = path + '/web'

trans = Translator()

eel.init(web_folder)

@eel.expose
def translate(data, src_lang, des_lang):
    my_text = data
    t = trans.translate(my_text, src = src_lang, dest = des_lang)
    # print(f'{t.origin}->{t.text}')
    output_data = f'{t.text}'
    return output_data

eel.start("index.html", size=(1000,700))