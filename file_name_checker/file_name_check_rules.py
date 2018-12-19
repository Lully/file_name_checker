# coding: utf-8

"""
Vérification du nommage des fichiers d'un répertoire

La liste des vérifications de nommage est dans la fonction check_filename()
"""

import re
from os import listdir
import os.path

from stdf import create_file, line2report

prefs = {}
try:
    with open('files/pref.json', encoding="utf-8") as prefs_file:
        prefs = json.load(prefs_file)
except FileNotFoundError:
    pass








def launch_analyse(output_filepath, directory_name, 
                   extension_files, checkrules,
                   get_exceptions, get_subdirectories):
    errors_list = []
    output_file = create_file(output_filepath)
    output_file.write(f"\nRépertoire analysé : {directory_name}")
 
    errors_list = analyse_dir(directory_name, errors_list, 
                              output_file,
                              extension_files, checkrules,
                              get_exceptions, get_subdirectories)
    if (errors_list == []):
        output_file.write("Aucune erreur trouvée, tout est parfait")
    else:
        output_file.write(f"\nTotal : {str(len(errors_list))} erreur(s) de nommage constatée(s)")


def analyse_dir(directory_name, errors_list, 
                output_file, extension_files, checkrules,
                get_exceptions, get_subdirectories):
    """
    Analyse d'un répertoire
    """
    list_files = listdir(directory_name)
    output_file.write(f"\n\n{str(len(list_files))} noms de fichiers analysés\n\n")
    for filename in list_files:
        filename = os.path.join(directory_name, filename)
        test_file = isFile(filename)
        if test_file:
            check_error, check_error_extension = check_filename(filename,
                                                                output_file, 
                                                                errors_list,
                                                                extension_files,
                                                                checkrules,
                                                                get_exceptions)
            if check_error or check_error_extension:
                errors_list.append(filename)
        elif get_subdirectories:
            subdir_name = os.path.join(directory_name, filename)
            analyse_dir(subdir_name, errors_list, output_file)
    return errors_list


def check_filename(filename, output_file, errors_list,
                   extension_files, checkrules,
                   get_exceptions=1):
    """
    Application des règles de contrôle sur le nom d'un fichier
    Si le nom n'est pas conforme, il est ajouté au fichier en sortie
    """
    check_error = False
    filename_beginning = filename[:-4]
    filename_end = filename[-3:].upper()
    # 1er test
    test_filename = re.fullmatch(checkrules, filename_beginning)
    
    if test_filename is None:
        if (get_exceptions == 2):
            check_error = False
        else:
            check_error = True
    # 2e test
    check_error_extension = False
    if (filename_end not in extension_files):
        if (get_exceptions == 2):
            check_error_extension = False
        else:
            check_error_extension = True
    
    if check_error:
        if (errors_list == []):
            line2report(["Liste des erreurs constatées\n"], output_file)
        line2report([filename, "erreur de nommage"], output_file)
    if check_error_extension:
        if (errors_list == [] and check_error is False):
            line2report(["Liste des erreurs constatées\n"], output_file)
        line2report([filename, 
                     f"Problème dans l'extension du fichier"], output_file)
    return check_error, check_error_extension


def isFile(filename):
    """
    Si c'est un fichier : retourne True. Sinon, retourne False
    """
    try:
        listdir(filename)
        return False
    except NotADirectoryError:
        return True


def eot(output_filepath):
    print("\n\nUn fichier listant les erreurs, nommé \"rapport erreurs de nommage.txt\"\n\
a été généré dans le même dossier que vos images.")
    osCommandString = "notepad.exe " + output_filepath
    os.system(osCommandString)


if __name__ == "__main__":
    print("-"*20, introduction_text, "-"*20, "\n\n")
    directory_name = input("\nIndiquer le chemin du répertoire où analyser les noms des fichiers : ")
    output_filename = prefs["output_filename"]
    extensionfile_list = prefs["extensionfile_list"]
    check_name_rule = prefs["check_name_rule"]
    output_filepath = os.path.join(directory_name, output_filename)
    launch_analyse(output_filepath, directory_name)
    eot(output_filepath)
