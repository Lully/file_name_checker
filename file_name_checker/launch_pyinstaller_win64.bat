:1.Lance la compilation du code source
:2. Nettoie le répertoire build, renomme dist en "verification_noms_de_fichiers" et y place le raccourci pour le lancement du fichier
:3. Compresse le répertoire obtenu
:4. Supprime le répertoire initial "verification_noms_de_fichiers" 
@echo off
set /p version="version: "
pyinstaller form.py
rd /s /q build
copy file_name_checker.bat dist
mkdir dist\config
copy config\prefs.json dist\config\prefs.json
rename dist file_name_checker
"C:\Program Files\7-Zip\7z" a -tzip ..\bin\file_name_checker_%version%.zip file_name_checker/
rd /s /q file_name_checker