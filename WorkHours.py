#!/usr/bin/env python
import PySimpleGUI as sg
from datetime import datetime
import json
from os import listdir
from os.path import isfile, join

from PySimpleGUI.PySimpleGUI import P

ICON = b'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'

class Project:
    def __init__(self, initial_data):
        for key in initial_data:
            setattr(self, '_'.join(key.split()), initial_data[key])

    def __str__(self) -> str:
        return self.project_name

    def create_table(self):
        # print(dir(self))
        # print(self.entries)
        table = [[dic['start time'], dic['end time'], dic['work duration'], dic['description']] for dic in self.entries]
        return table

    def calculate_hours(self):
        hours = 0
        for entry in self.entries:
            hours += float(entry['work duration'])
        self.total_time = hours


def retrieve_data():
    with open('data.json') as file:
        return json.load(file)

def retrieve_projects(project_order):
    projects = []
    files = [f for f in listdir('./projects') if isfile(join('./projects', f)) and f != '.gitignore']
    for file in files:
        with open(f'./projects/{str(file)}') as json_file:
            json_data = json.load(json_file)
            json_data['project name'] = file.split('.')[0]
            # print(json_data)
            projects.append(Project(json_data))
        
    for order in project_order:
        projects.insert(project_order.index(order), projects.pop(projects.index([i for i in projects if str(i) == order][0])))
    return projects

data = retrieve_data()
projects = retrieve_projects(data['project order'])

HEADINGS = ['Start', 'End', 'Total', 'Description']

# ------ Window Layout ------

def create_project_column(project, focused_col):
    layout = [
        [sg.Column(layout=[[sg.Multiline(default_text=project.project_description, size=(55,2), disabled=True)]], pad=(0,0)), sg.Column(layout=[[sg.Multiline(default_text=f"total time:\n{project.total_time} hours", size=(21,2), disabled=True)]], pad=(0,0))],
        [sg.Table(values=project.create_table(),
                    key = f'-TABLE_{project.project_name}-',
                    headings=HEADINGS,
                    header_background_color='default',
                    def_col_width=100,
                    col_widths=[18,18,5,24],
                    auto_size_columns=False,
                    justification='center',
                    num_rows=8,
                    hide_vertical_scroll=False,
                    row_height=25,
                    enable_events=True)]
    ]
    return sg.Column(layout, key=f'-COL_{project.project_name}-', pad=(0,0), visible=True if focused_col == project.project_name else False)

def create_row_of_cols():
    row = []
    for project in projects:
        row.append(create_project_column(project, data['focused']))
    return row

def create_layout():
    combo = list(projects)
    combo.append(f"{' '*74}more options..")

    # Column that contains the main program. The table and the function row at the bottom for timing
    main_col = [
        create_row_of_cols(),
        [sg.pin(sg.Button('Start', size=(5,1))), sg.pin(sg.Button('Stop', size=(5,1))),
        sg.Input(key="-TIME_STARTED-", size=(12,1), default_text='time start', readonly=True),
        sg.Input(key="-TIME_STOPPED-", size=(12,1), default_text='time stopped', readonly=True),
        sg.Input(key="-WORK_DURATION-", size=(12,1), default_text='work duration', readonly=True),
        sg.Input(key="-DESCRIPTION-", size=(20,1), default_text='description of work'),
        sg.Button('Add', size=(9,1))
        ]
    ]

    more_options_col_project_form = [
        [sg.Input(key='-INPUT_PROJECT_NAME-',size=(21,1), default_text='project name')],
        [sg.Multiline(k='-INPUT_PROJECT_DESCRIPTION-', size=(20,8), default_text='project description')],
        [sg.Button('add project', size=(19,1))]
    ]

    projects_listbox = [str(i) for i in projects]
    add_project_spacing = 8
    projects_listbox.insert(0, ' '*add_project_spacing+'add new project')

    more_options_col = [
        [sg.Column([[sg.Listbox(projects_listbox, k='-LISTBOX_PROJECTS-', size=(20,11), enable_events=True, select_mode=sg.SELECT_MODE_SINGLE)]]), sg.Column(more_options_col_project_form, vertical_alignment='top')]
    ]

    combo_default_spacing = 74 if data['focused'] not in data['project order'] else 0

    layout = [
        [sg.Combo(combo, key='-COMBO_PROJECTS-', default_value=' '*combo_default_spacing+data['focused'], readonly=True, size=(78,1), enable_events=True)],
        [sg.Column(main_col, key='-COL_MAIN-', pad=(0,0)), sg.Column(more_options_col, key='-COL_MORE_OPTIONS-', pad=(0,0), size=(600,350), expand_x=True)],
        [sg.Text(key='-OUTPUT-', text='not started', background_color='#ffffff', text_color='#696969', pad=((0,0),(5,0)), size=(80,1))]
    ]
    return layout

# ------ Create Window ------
def create_window(location=(None, None)):
    window = sg.Window('WorkHours', create_layout(), finalize=True, icon=ICON, margins=(0,0), location=location)
    window['Stop'].update(visible=False)
    window['Add'].update(disabled=True)
    window['-COL_MORE_OPTIONS-'].update(visible=False)

    focus = data['focused']
    project_names  = [project.project_name for project in projects]
    window['-COL_MORE_OPTIONS-'].update(visible=True if focus not in project_names else False)
    window['-COL_MAIN-'].update(visible=False if focus not in project_names else True)

    return window

def remake_window():
    save()
    global window
    old_window = window
    x, y = old_window.current_location()
    old_window.close()
    window = create_window((x, y-60))

window = create_window()

# ------ Functions ------
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
    window['-WORK_DURATION-'].update(f"{round(work_hours, 3)}")

    window['-OUTPUT-'].update('timer stopped')
    global timer_started
    timer_started = False

def add_entry():
    window['Start'].update(disabled=False)
    window['Add'].update(disabled=True)
    print(data['focused'])

    for project in projects:
        if data['focused'] == project.project_name:
            project.entries.append(
                {
                    "start time": values['-TIME_STARTED-'],
                    "end time": values['-TIME_STOPPED-'],
                    "work duration": values['-WORK_DURATION-'],
                    "description": values['-DESCRIPTION-']
                }
            )
            project.calculate_hours()

    remake_window()

    window['-TIME_STARTED-'].update('time started')
    window['-TIME_STOPPED-'].update('time stopped')
    window['-WORK_DURATION-'].update('work duration')
    window['-DESCRIPTION-'].update('description of work')

def update_timer_text():
    time_started = datetime.strptime(values['-TIME_STARTED-'], "%H:%M:%S  %d/%m/%Y")
    time_stopped = datetime.now()
    work_duration = time_stopped - time_started
    work_duration = str(work_duration).split('.')[0]

    window['-OUTPUT-'].update(f'time elapsed: {work_duration}')

def change_focus():
    new_focus = values['-COMBO_PROJECTS-']
    print(str(new_focus))
    for project in projects:
        window[f'-COL_{project.project_name}-'].update(visible=True if project == new_focus else False)

    window['-COL_MORE_OPTIONS-'].update(visible=True if new_focus not in projects else False)
    window['-COL_MAIN-'].update(visible=False if new_focus not in projects else True)
    window['-OUTPUT-'].update(str(new_focus).strip())

    data['focused'] = str(new_focus)

def add_project():
    project_data = {
        "project name": values['-INPUT_PROJECT_NAME-'],
        "project description": values['-INPUT_PROJECT_DESCRIPTION-'],
        "total time": 0,
        "entries": []
    }
    projects.append(Project(project_data))
    data['project order'].append(project_data['project name'])
    remake_window()

def save():
    with open('./data.json', 'w') as data_file:
        if data['focused'] not in data['project order']:
            data['focused'] = data['focused'].strip()
        json.dump(data, data_file, indent=4)
    for project in projects:
        project_data = dict(vars(project))
        print(project_data)
        project_data.pop('project_name')
        print(vars(project))
        with open(f'./projects/{str(project)}.json', 'w') as project_file:
            json.dump(project_data, project_file, indent=4)

def change_listbox_project_view():
    if values['-LISTBOX_PROJECTS-'][0].strip() == 'add new project':
        window['-INPUT_PROJECT_NAME-'].update('project name')
        window['-INPUT_PROJECT_DESCRIPTION-'].update('project description')
        window['add project'].update(disabled=False)
    else:
        for project in projects:
            if values['-LISTBOX_PROJECTS-'][0] == str(project):
                window['-INPUT_PROJECT_NAME-'].update(project.project_name)
                window['-INPUT_PROJECT_DESCRIPTION-'].update(project.project_description)
                window['add project'].update(disabled=True)



switch_case_dict = {
    'Start': start_timer,
    'Stop': stop_timer,
    'Add': add_entry,
    '-COMBO_PROJECTS-': change_focus,
    'add project': add_project,
    '-LISTBOX_PROJECTS-': change_listbox_project_view
}

timer_started = False

# ------ Event Loop ------
while True:
        
    event, values = window.read(timeout=1000)

    if timer_started:
        update_timer_text()

    if event != '__TIMEOUT__':
        print(event, values)
        print(data)

    if event == sg.WIN_CLOSED:
        break

    if event in switch_case_dict:
        switch_case_dict[event]()

save()
window.close()
