import PySimpleGUI as sg
from file_name_grab import get_files, recursive_get_files

sg.theme("DefaultNoMoreNagging")  # Add a touch of color
# All the stuff inside your window.
col = [
    [sg.Text("Input Folder")],
    [
        sg.Input(key="input_dir", change_submits=True),
        sg.FolderBrowse(),
    ],
    [
        sg.Text("Output Folder"),
        sg.Checkbox(
            "Same as input?", default=True, key="output_checkbox", enable_events=True
        ),
    ],
    [sg.Input(key="output_dir"), sg.FolderBrowse()],
    [
        sg.Radio(
            "All files",
            "RADIO1",
            default=True,
            key="all_file_radio",
            enable_events=True,
        ),
        sg.Radio("Specific extension", "RADIO1", enable_events=True),
        sg.Combo(
            [
                ".pdf",
                ".jpg",
                ".jpeg",
                ".png",
                ".doc",
                ".docx",
                ".xlsx",
                ".xlsm",
                ".txt",
                ".zip",
                ".csv",
                "other",
            ],
            key="extension_dropdown",
            enable_events=True,
        ),
        sg.Input(size=(6, 1), key="extension_typed_input", enable_events=True),
    ],
    [
        sg.Checkbox(
            "Search subfolders?",
            default=False,
            key="subfolder_check",
            enable_events=True,
        ),
        sg.Text("", key="warning_text", size=(35, 2), enable_events=True),
    ],
]
layout = [
    [sg.Column(col)],
    [
        sg.Submit(key="submit"),
        sg.Cancel(key="Exit"),
        sg.Text("", key="output_text", size=(35, 4)),
    ],
]
window = sg.Window("File Finder", layout)

while True:  # The Event Loop
    event, values = window.read()
    input_dir = values["input_dir"]
    # --
    if values["output_checkbox"] == True:
        output_dir = None
        window["output_dir"].update(values["input_dir"])
    else:
        output_dir = values["output_dir"]
    # --
    try:
        if values["all_file_radio"] == True:
            extension = ".*"
        else:
            extension = values["extension_dropdown"]
            if extension == "other":
                extension = values["extension_typed_input"]
        # --
        if values["subfolder_check"] == True:
            window["warning_text"].update(
                "Caution: Subfolder search may take a long time"
            )
            files = recursive_get_files(
                input_dir=input_dir, extension=extension, output_dir=output_dir
            )
        else:
            files = get_files(
                input_dir=input_dir, extension=extension, output_dir=output_dir
            )
        # --
    except FileNotFoundError:
        continue
    if event == "submit":
        window["output_text"].update(files)
    if event == sg.WIN_CLOSED or event == "Exit":
        break

window.close()
