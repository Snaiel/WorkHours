#!/usr/bin/env python
import PySimpleGUI as sg
import random
import string
from datetime import datetime, timedelta

ICON = b'iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAYAAABccqhmAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAxOSURBVHgB7d1fbhzHEcfx6t6VkUfnBN6cwGIukL1BxCABEsWAeQMjR8gJnNxABvJHgOFQPoHHzwFC5QbrG/glSCByejJLzpJLcrnc2a7q7pn5fgBbD7JErcWp7q7+dY8IAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB3nCj759efLefz5nPRVodvT37993eSycU3r8/Eu1+Iihd/ODl986NkcHF+9rHI5ZdSosx/x33ofj9sq/94cvp2JYnMRdl8HtpvbHcmyhrvftr+kO+bw7t1UVuKgjp8+L794Y1kcfWy/deZFCg494Pk/DvuoXHN0onTH+hEvmr/WUkiXpSdnP7tffuD+ujmnPtUMrkZNXUe/rV22vVSMgnSZPvaKI96Aei8F32L7kHM4Er1ofEmU8cDv7Y02b42ymNSAEJo/i0m/pdl9AohLEXXy3zFzC0E6JgUgKbxlRgIwWUpADYjdvpi1hUdlgC4ZVIAZrN5JQbaBzFXH0D9oclTzK54+HGPSQHotrhWos5lGDVfr7+m+nTde/9LSYwGIB6yagK2y4DwvehLvnYO4pZiI/nD6Bqm/7jPrgA4b7ET0PrPQhIy7Jp/fHH+m6QPpHPyiQBbzApA++BUYqAOLxKPYnbLjhDmS0lrKcAWswJgFghKOHVulxuL9oeFGEnZ1Ox6GcA9ZgWgo74MSBmiqWvrrrlZf+GRuvYLAR4wLQBGgaCFJOKcegDooWTpxgSfBQNkWgCMAkFt8+y3C0kgxWyjDh9eSQIZMxQomGkBsAoE1cEvxViq1FzCngY9ADxiWgCsAkFpHpo0qbkUs4yumZnp7AFKZt0ENAkEtfvZCzFmcADoKebhJvtmJobKvgAYBIKcsx810x7ZtT0Y1DYAKQDYybwAGAWCUjQCkz001geDvBcagNjJvABYBYJm/iOzb+qL88+WknDNbH8wyC0E2MG8AHTUlwGXV5c/EyMZTs2ZfT3uAMA+SQqARSCo7QMsxUiGa7MMDwbRAMTTkhQAi0CQ7SWh6e8dsDoYxB0A2CdJATAKBJnEaK0PAD3FKqlnNJtR7+kgjyQFwO6GIIPts/BhKVlYLWncQvQZ3fWA1FI1AU0CQRbbZ41Ld0LvAauDQQb3GVrd+ozU0hUAg0CQxbTZuXx75toHg7rtTG0m27rII1kBsAkE6c4Acm+ZqZ9xCGEhytrR3+KuR2SSrAAYBYKUc/R5t8y048fBoJi9mM+/E4xGsgLQMWge6V0SGkJQnYIfQbWgWSyR6vDfHwSjkbQAWDSPNC8JLePSDNWdDe0ZwI8np1+zAzAiSQuASSBI95t8KZlp7WwYvdCEh39kkhYAi0CQ1rrZqGPem9bBIItLQGkAjk/SAmAUCFqIgoIisyp/Dos7ALwPlWBUUjcBLQJBKncDZDgA9BSVg0E2F5r8hCXAyKQvAAaBIJ1LQuMTgO0U+c+iQOlgkPYM4H03g8OIJC8AFoGg2EagVsOsnSK/E4UlTuxuRLeVSAMQz0peACwCQdGXhAad0fLk9G2ls8SJnY0YBJq8VILRSV4AOqqjSewloUoHgKr1v1zjKokXdTDIpKEZPnAAaISyFACDQFBUI1DjANDtZ1LqlMccDDJoaBIAGqksBcAiEHTsJaFaB4C69f96GbAShT5AXF/DLUQXD/9IZSkAFoGgYy8Jreurpai42yLT6AMcu41ncaKRANB4zSWD9XbSxfnvV6J49VZ3SeifpKebt+Y6iVRtb5Gttzrb3/FziXN9MKj/1tvVYANA3vtPL755fSZD4NwnMgJZCsDaepR0Ti+ueuwloRoHgB72NLzU7XJg9qVEuz4YVPX5FesGoP60LlUAqHkl3h3d+0B/uXYBLAJBx3bOlxLp4Rn5rg8QvdV5zMEg1xAAwuGyFQCbG4L6HaXVOgBUB/9ojdzOcL6VSMccDGp3NLSnpjQARyxbAbAIBPUdMZX2y3eOkEoznGP+fEvRRABo1LIVgI7q6NJ3Pd9++Oijt091yJVmOL0OBnWRZl0EgEYtawHQDwT1TvRFPzBP3ZGnNcPpczDI4A4AAkAjl7UAGASCDm4Eah0AqveOkPGzgD6zmpstTVU8/COXtQDYvDLswEtCdQ4Ave86/k98CZf0YJD2nYYEgMYvawGwuCHo0EtClQ4A7R0hlfoAfbY3VXsA3AA0frmbgOo3BB2aoW+3y6IPzMz87N2+n9fqAxxyMKh7qWn0kuY+bgAau/wFQDkQdEiGXusNwPVhHfLoz3dIUatr9QgwAaAJyF4ADAJBi+f+A52HpVntW/9vBBGFQNDzRc3gElBG/wnIXgAMAkHP3g2g0y0/7OIPL04lEPRcH8B75ZeaEgCahOwFoKM62jx3SahKt/zgB2SuVOCeizm7hWgiADQJRRQA7UDQvjVzN5IuJdaBD0i3jo4ucPtizgZ3ABAAmogiCoB2IGj/CK+1/j/8AdHIA+w/GKTfABRMQhEFwCAQ9OQDEUL8+r9ppNeMxYvKevrpz6R8CSgBoOnIdiHINoMbgq4bgbu69BpvzHEzd97rF1z3AS4l0vXBoF0zj5tLQKNvNbr7/TIFgNrC+pVz7o0MQvii/X/+bD6jdEUUgDXtG4K6S0JXO34qfrTs2SDrClwlkb2H7mDQjum5W4iqPAGgpmlWP//VXysZgH/943dnbbGSoStlF0A9ELTrklClA0BHNcg0Gp17ehuaSwACQBNSTAHQDgS5HVn/oPD+v3aUOmp93Dbx3km0x39+g9ea0wCckGIKgHYgaNcloRovzGgLQCVHmWs8WI8PBoWwEE0EgCalmALQ0Rx9dpyic9FTZe+vKjmCVh7g4cGgoP0WYAJAk1JUAdC/IeguPad0ACgqIKOxvfYw5KR8BwABoIkpqgBoB4K203NKp+WiHg6Nz7djG1O1ASiYlKIKgHYgaHt01DgAFELcVd9Kn+/2YJDWtWYbBICmp6gCoH9D0F3XXCMA5H0TNUJq9QE2SxvtS0C5AWh6igkCbSgHgrYagZexU+V2ffy2kkjrUbYtRlF/lm5pU93cAaAZRuEGoKkpbRfA4JVh60tC86//N7zC77M5GKQxq9lCAGiCiisA2oGg9SWhGgeA1NbH/iOFQNBt448GIKIUVwDUA0HtQ6Kz/tdZHyv1OdaHnZaieQkoAaBJKq4AdNRGo+7hjx4pNdb/Gzo3Ic+/EE0EgCapyAKgHAjS2CqrRJFrDrtPcL/mleghADRRRRYAg1eGRVFPKJa33cbDP1FFFgCbV4Ydr13/azTubnUXlaykEASApqvIAmDxyrA4+vvj2m9EikEAaLpKbQKW9IBUFvvj+nmHGASApqrcAlDIA6J/QvGGl1p1WRGBANCEFVsADF4ZdpQX8/l3YqDrA5Tw4DH6T1ixBcDglWFHqYM3W4q0y5zo9wZGIwA0acUWgE7u0cl0elzEMocA0KQVXQCs1t89vr5pI7KAZQ4BoIkrugD4zDMAq/X/RgHLHB7+iSt7CZB5f7pOMj3ONwsgAISiC0DmxNz7Xa8W06bx4tBjEQBC6U3AnIGgJNPjvH0AAkBTV34ByNQpn/lZkqBOxj4AASCUXwC8uCwFoE67PZbjMzL6o/wC0L1SK/FI1axSrP83gkj6QBABIMgACoDeVdp9aFzYcbgssxwCQJBBzAAyBIISj44np3+pJO0shwAQrg2iACQPBIU6x85Dys/Iw49rgygAaQNBadf/GynzAASAsDGIApAyENQ0kmVt7CXdsoMAEDaGMQOQdIEgN3PnkkXK3Q4CQLgxnAKQKhCUqTuecLeDABBuDaYAJNoqy9odT7TbweiPW4MpACmmyE2TtznmvbePHxMAwpbBFIAUU+S2AFSS1dx+dCYAhC0DmgHYT5G9v6okowRFjgAQ7hlUAfATeDiM9+h5+HHPoAqAcSCoiIfD8r2IBIDw0KAKgGUgKIQCrugW2/ciEgACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJuz/bjaRBj3ipSMAAAAASUVORK5CYII='

# ------ Some functions to help generate data for the table ------
def word():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
def number(max_val=1000):
    return random.randint(0, max_val)

def make_table():
    data = [[j for j in range(4)] for _ in range(20)]
    for i in range(0, 20):
        data[i] = [*[number() for _ in range(3)], word()]
    return data


combo = ['PySImpleGUI', 'Nemix']

# ------ Make the Table Data ------
data = make_table()
headings = ['Start', 'End', 'Total', 'Description']

# ------ Window Layout ------
layout = [
    [sg.Combo(combo, default_value=combo[0], readonly=True, size=(78,1))],
    [sg.Column(layout=[[sg.Multiline(size=(55,2))]], pad=(0,0)), sg.Column(layout=[[sg.Multiline(size=(21,2))]], pad=(0,0))],
    [sg.Table(values=data[1:][:],
                    headings=headings,
                    header_background_color='default',
                    def_col_width=100,
                    col_widths=[15,15,5,30],
                    auto_size_columns=False,
                    justification='left',
                    num_rows=8,
                    key='-TABLE-',
                    hide_vertical_scroll=False,
                    row_height=25,
                    enable_events=True)],
    [sg.pin(sg.Button('Start', size=(5,1))), sg.pin(sg.Button('Stop', size=(5,1))),
    sg.Input(key="-TIME_STARTED-", size=(12,1), default_text='time start', readonly=True),
    sg.Input(key="-TIME_STOPPED-", size=(12,1), default_text='time stopped', readonly=True),
    sg.Input(key="-WORK_DURATION-", size=(12,1), default_text='work duration', readonly=True),
    sg.Input(key="-WORK_DURATION-", size=(20,1), default_text='description of work'),
    sg.Button('Add', size=(9,1))
    ],
    [sg.Text(key='-OUTPUT-', text='not started', background_color='#ffffff', text_color='#696969', pad=((0,0),(5,0)), size=(80,1))]
]

# ------ Create Window ------
window = sg.Window('WorkHours', layout, finalize=True, icon=ICON, margins=(0,0))
window['Stop'].update(visible=False)
window['Add'].update(disabled=True)

def start_timer():
    window['Start'].update(visible=False)
    window['Stop'].update(visible=True)

    time_started = datetime.now()
    window['-TIME_STARTED-'].update(time_started.strftime("%H:%M:%S  %d/%m/%Y"))

    window['-OUTPUT-'].update('timer started')
    global timer_started
    timer_started = True

def stop_timer():
    window['Start'].update(visible=True, disabled=True)
    window['Stop'].update(visible=False)
    window['Add'].update(disabled=False)
    window['-OUTPUT-'].update('timer started. ')

    time_stopped = datetime.now()
    window['-TIME_STOPPED-'].update(time_stopped.strftime("%H:%M:%S  %d/%m/%Y"))

    time_started = datetime.strptime(values['-TIME_STARTED-'], "%H:%M:%S  %d/%m/%Y")

    work_duration = time_stopped - time_started
    work_duration = work_duration.total_seconds()
    work_hours = work_duration / 3600
    window['-WORK_DURATION-'].update(f"{round(work_hours, 3)}h")

    window['-OUTPUT-'].update('timer stopped')
    global timer_started
    timer_started = False

def add_entry():
    window['Start'].update(disabled=False)
    window['Add'].update(disabled=True)

def update_timer_text():
    time_started = datetime.strptime(values['-TIME_STARTED-'], "%H:%M:%S  %d/%m/%Y")
    time_stopped = datetime.now()
    work_duration = time_stopped - time_started
    work_duration = str(work_duration).split('.')[0]

    window['-OUTPUT-'].update(f'time elapsed: {work_duration}')


switch_case_dict = {
    'Start': start_timer,
    'Stop': stop_timer,
    'Add': add_entry
}

timer_started = False

# ------ Event Loop ------
while True:
        
    event, values = window.read(timeout=1000)

    if timer_started:
        update_timer_text()

    if event != '__TIMEOUT__':
        print(event, values)

    if event == sg.WIN_CLOSED:
        break

    if event in switch_case_dict:
        switch_case_dict[event]()

window.close()
