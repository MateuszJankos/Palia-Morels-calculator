#impurtuje nicegui
from nicegui import ui
#zawartośc programu

GW = ui.slider(min=0, max=30, value=21)
ui.label().bind_text_from(GW, 'value')




#rozpoczyna program
ui.run(title='Morel Calculator')