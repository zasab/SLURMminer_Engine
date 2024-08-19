@echo off

REM Get the current script directory (where pm4pyyy is assumed to be located)
set SCRIPT_DIR=%~dp0

REM Automatically find the site-packages directory for the active Python environment
for /F "delims=" %%i in ('where python') do set PYTHON_PATH=%%i

REM Find the site-packages directory
for /F "usebackq tokens=* delims=" %%i in (`%PYTHON_PATH% -c "import site; print(site.getsitepackages()[0])"`) do set SITE_PACKAGES=%%i

REM Define the source and destination paths automatically
set source1=%SCRIPT_DIR%custom_pm4py\lxml.py
set destination1=%SITE_PACKAGES%\pm4py\objects\bpmn\importer\variants\lxml.py

set source2=%SCRIPT_DIR%custom_pm4py\obj.py
set destination2=%SITE_PACKAGES%\pm4py\objects\bpmn\obj.py

REM Copy the files to their respective locations
copy /Y "%source1%" "%destination1%"
copy /Y "%source2%" "%destination2%"

echo Files replaced successfully!
pause
