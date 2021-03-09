#!/usr/bin/env python
import PySimpleGUI as sg
import random
import string

# ------ Some functions to help generate data for the table ------
def word():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
def number(max_val=1000):
    return random.randint(0, max_val)

def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [word() for __ in range(num_cols)]
    for i in range(1, num_rows):
        data[i] = [word(), *[number() for i in range(num_cols - 1)]]
    return data


combo = ['PySImpleGUI', 'Nemix']

# ------ Make the Table Data ------
data = make_table(num_rows=15, num_cols=6)
headings = ['Start', 'End', 'Total', 'Description']

# ------ Window Layout ------
layout = [
    [sg.Combo(combo, default_value=combo[0], readonly=True, size=(75,1))],
    [sg.Table(values=data[1:][:],
                    headings=headings,
                    header_background_color='default',
                    def_col_width=100,
                    col_widths=[15,15,5,25],
                    auto_size_columns=False,
                    # background_color='light blue',
                    justification='left',
                    num_rows=8,
                    key='-TABLE-',
                    hide_vertical_scroll=False,
                    row_height=25,
                    enable_events=True,
                    tooltip='This is a table')],
    [sg.Button('Start'), sg.Button('Stop')]
        ]

# ------ Create Window ------
window = sg.Window('The Table Element', layout, size=(590, 300), finalize=True)

previous_selection = []

# ------ Event Loop ------
while True:
    event, values = window.read()
    print(event, values)

    print(previous_selection)
    if values['-TABLE-'] == previous_selection:
        window['-TABLE-'].update(select_rows=[])
        previous_selection = values['-TABLE-']
    else:
        previous_selection = values['-TABLE-']

    if event == sg.WIN_CLOSED:
        break
    if event == 'Stop':
        window['-TABLE-'].update(select_rows=[])

window.close()
