#impurtuje nicegui
from nicegui import ui
import math
#zawartośc programu

#Pytamy ile glow worm farm posiadasz
ui.label('Ilość GLOW WORM FARM:')
GW = ui.slider(min=0, max=30, value=21)
ui.label().bind_text_from(GW, 'value')

#Pytamy ile moreli aktualnie się znajduje jeszcze
ui.label('How many morels left? ')
Morel = ui.slider(min=0, max=30, value=0)
ui.label().bind_text_from(Morel, 'value')

#Tworzymy guzik do aktywacji obliczeń
ui.button('Calculate!', on_click=lambda: ui.notify('Thinking...'))

#rozpoczyna program
ui.run(title='Morel Calculator', dark=True)