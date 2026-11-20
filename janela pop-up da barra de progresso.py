import PySimpleGUI as sg
for i in range(1000):
    sg.one_line_progress_meter(
        'progress_bar',
        i + 1,
        1000,
        'this progress bar key',
        'this is a progress bar '
        
        )