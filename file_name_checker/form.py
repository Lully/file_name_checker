# coding: utf-8

from tkinter import filedialog
import tkinter as tk
from time import gmtime, strftime
import json
from file_name_check_rules import *

prefs = {}
try:
    with open('files/prefs.json', encoding="utf-8") as prefs_file:
        prefs = json.load(prefs_file)
except FileNotFoundError:
    pass

log_file = None
try:
    log_file = open('files/file_name_checker_logs.txt', 
                    "a", encoding="utf-8")
except FileNotFoundError:
    log_file = open('files/file_name_checker_logs.txt', 
                    "w", encoding="utf-8")

selected_directory = [""]

def formulaire_main(output_filename_default, 
                    extensionfile_list_default,
                    check_name_rule_default,
                    introduction_text_default):
    couleur_fond = "white"
    couleur_bouton = "#e1e1e1"

    [master,
     zone_alert_explications,
     zone_access2programs,
     zone_actions,
     zone_ok_help_cancel,
     zone_notes] = main_form_frames(
         "Programme de contrôle de nommage\
des fichiers",
         couleur_fond,
         couleur_bouton)

    frame1 = tk.Frame(zone_actions, 
                      bg=couleur_fond, pady=20, padx=20)
    frame1.pack(side="left", anchor="w")

    frame_header = tk.Frame(frame1, 
                      bg=couleur_fond, pady=5, padx=20)
    frame_header.pack()

    frame_directory_selection = tk.Frame(frame1, 
                      bg=couleur_fond, pady=5, padx=20)
    frame_directory_selection.pack()

    option_outputfilename = tk.Frame(frame1, 
                      bg=couleur_fond, pady=5, padx=20)
    option_outputfilename.pack()

    option_extensions_files = tk.Frame(frame1, 
                      bg=couleur_fond, pady=5, padx=20)
    option_extensions_files.pack()

    option_checkrules = tk.Frame(frame1, 
                      bg=couleur_fond, pady=5, padx=20)
    option_checkrules.pack()

    option_exceptions = tk.Frame(frame1, 
                      bg=couleur_fond, pady=5, padx=20)
    option_exceptions.pack()

    frame_launch = tk.Frame(frame1, 
                      bg=couleur_fond, pady=5, padx=20)
    frame_launch.pack()

    frame_help_cancel = tk.Frame(
        zone_ok_help_cancel, bg=couleur_fond, pady=10, padx=20)
    frame_help_cancel.pack()

    tk.Label(frame_header, text="Sélectionner un répertoire",
             bg=couleur_fond, fg="#365B43", font="Arial 11 bold").pack(anchor="w")
    tk.Label(frame_header, text="\n", bg=couleur_fond).pack()

    download_zone(
        frame_directory_selection,
        "Sélectionner un répertoire",
        selected_directory,
        couleur_fond,
    )

    """
    Valeurs par défaut, éditables
    output_filename_default, 
    extensionfile_list_default,
    check_name_rule_default
    """
    tk.Label(option_outputfilename, bg=couleur_fond,
             text="Nom du rapport ",
             justify="left").pack(side="left")
    outputfilename = tk.Entry(option_outputfilename, width=40, bd=2)
    outputfilename.insert(string=output_filename_default,
                          index=0)
    outputfilename.pack()
    
    tk.Label(option_extensions_files, bg=couleur_fond,
             text="Extensions autorisées ",
             justify="left").pack(side="left")
    extensions_files = tk.Entry(option_extensions_files, width=40, bd=2)
    extensions_files.insert(string=",".join(extensionfile_list_default),
                            index=0)
    extensions_files.pack()
    

    tk.Label(option_checkrules, bg=couleur_fond,
             text="Règles de nommage ",
             justify="left").pack(side="left")
    checkrules = tk.Entry(option_checkrules, width=40, bd=2)
    checkrules.insert(string=check_name_rule_default,
                      index=0)
    checkrules.pack()

    get_exceptions = tk.IntVar()
    tk.Radiobutton(
        option_exceptions,
        bg=couleur_fond,
        text="Identifier les fichier non conformes aux règles",
        variable=get_exceptions,
        value=1,
        justify="left").pack()
    tk.Radiobutton(
        option_exceptions,
        bg=couleur_fond,
        text="Identifier les fichier correspondant aux règles",
        variable=get_exceptions,
        value=2,
        justify="left").pack()
    get_exceptions.set(1)

    get_subdirectories = tk.IntVar()
    get_subdirectories_check = tk.Checkbutton(
        option_exceptions,
        bg=couleur_fond,
        text="Chercher dans tous les sous-dossiers",
        variable=get_subdirectories,
        justify="left",
    )
    get_subdirectories_check.pack(anchor="w")
    get_subdirectories.set(1)

    tk.Label(frame_launch, bg=couleur_fond, text="\n").pack()
    launch_button = tk.Button(frame_launch,
                              text="Lancer le contrôle\nsur le nommage\ndes fichiers",
                              command=lambda: launch(outputfilename.get(),
                                                     extension_files.get(),
                                                     checkrules.get(),
                                                     get_exceptions.get(),
                                                     get_subdirectories.get()),
                              padx=24,
                              pady=15,
                              bg="#9E1919",
                              fg="white",
                              font="Arial 9 bold")
    launch_button.pack()

    tk.Label(zone_ok_help_cancel,
             text=introduction_text_default, 
             pady=5, justify="left",
             bg=couleur_fond).pack(side="left", anchor="w")
    tk.Label(frame_help_cancel, text="\n",
             bg=couleur_fond, font="Arial 8 normal").pack()
    tk.mainloop()


def params2logfile(outputfilename, extension_files,
                   checkrules, get_exceptions,
                   get_subdirectories):
    get_exceptions_dict = {1: "Lister les fichiers ne correspondant pas aux règles",
                           2: "Lister les fichiers conformes aux règles de nommage"}
    get_subdirectories_dict = {0: "Ne pas analyser les sous-répertoires",
                          1: "Analyser les sous-répertoires"}
    
    log_file.write(f"""
Contrôle du {strftime("%Y-%m-%d %H:%M:%S", gmtime())}
Nom du fichier en sortie : {outputfilename}
Règles de contrôle : {checkrules}
Extensions de fichier : {extension_files}
Option : {get_exceptions_dict[get_exceptions]}
Option : {get_subdirectories_dict[get_subdirectories]}
""")


def launch(outputfilename, extension_files, checkrules,
           get_exceptions, get_subdirectories):
    params2logfile(outputfilename, extension_files,
                   checkrules, get_exceptions,
                   get_subdirectories)
    extension_files = extension_files.split(",")
    output_filepath = os.path.join(selected_directory[0], outputfilename)
    launch_analyse(output_filepath, selected_directory[0], 
                   extension_files, checkrules,
                   get_exceptions, get_subdirectories)
    eot(output_filepath)



def main_form_frames(title, couleur_fond, couleur_bordure):
    # ----------------------------------------------------
    # |                    Frame                         |
    # |            zone_alert_explications               |
    # ----------------------------------------------------
    # |                    Frame                         |
    # |             zone_access2programs                 |
    # |                                                  |
    # |              Frame           |       Frame       |
    # |           zone_actions       |  zone_help_cancel |
    # ----------------------------------------------------
    # |                    Frame                         |
    # |                  zone_notes                      |
    # ----------------------------------------------------
    master = tk.Tk()
    master.config(padx=10, pady=10, bg=couleur_fond)
    master.title(title)

    zone_alert_explications = tk.Frame(master, bg=couleur_fond, pady=10)
    zone_alert_explications.pack()

    zone_access2programs = tk.Frame(master, bg=couleur_fond)
    zone_access2programs.pack()
    zone_actions = tk.Frame(zone_access2programs, bg=couleur_fond)
    zone_actions.pack(side="left")
    zone_ok_help_cancel = tk.Frame(zone_access2programs, bg=couleur_fond)
    zone_ok_help_cancel.pack(side="left", anchor="w")
    zone_notes = tk.Frame(master, bg=couleur_fond, pady=10)
    zone_notes.pack()

    return [master,
            zone_alert_explications,
            zone_access2programs,
            zone_actions,
            zone_ok_help_cancel,
            zone_notes]

def download_zone(frame, text_bouton, selected_directory,
                  couleur_fond):
    frame_button = tk.Frame(frame)
    frame_button.pack()
    frame_selected = tk.Frame(frame)
    frame_selected.pack()
    display_selected = tk.Text(
        frame_selected, height=3, width=50, 
        bg=couleur_fond, bd=0, font="Arial 9 bold")
    display_selected.pack()
    # bouton_telecharger = download_button(frame,"Sélectionner un fichier","#ffffff")
    select_filename_button = tk.Button(
        frame_button,
        command=lambda: download_button(
            frame,
            text_bouton,
            frame_selected,
            display_selected,
            "#ffffff",
            selected_directory,
        ),
        text=text_bouton,
        padx=10,
        pady=10,
    )
    select_filename_button.pack()


def download_button(frame, text, frame_selected, text_path,
                    couleur_fond, selected_directory):
    if (selected_directory != []):
        text_path.delete(0.0, 1000.3)
    filename = filedialog.askdirectory(
        parent=frame, title="Sélectionner un répertoire"
        )
    selected_directory[0] = filename
    text_path.insert(0.0, filename)



if __name__ == "__main__":
    output_filename = prefs["output_filename"]
    extensionfile_list = prefs["extensionfile_list"]
    check_name_rule = prefs["check_name_rule"]
    introduction_text = prefs["introduction_text"]
    formulaire_main(output_filename, extensionfile_list, 
                    check_name_rule, introduction_text)