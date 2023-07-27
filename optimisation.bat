
@echo off
title OPTIMISATION
color 0a
cls
echo Attendez que le programme démarre...
echo.
echo Vous devrez peut-être fournir des informations d'identification administrateur.
echo.
echo Appuyez sur une touche pour continuer...
pause >nul
cd /d %~dp0
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)
echo.

:: Fonction pour exécuter une commande PowerShell
set "ps_command=powershell -Command "
set "ps_args=-NoProfile -NonInteractive -NoLogo -ExecutionPolicy Bypass "
set "ps_exe=%ps_command% %ps_args%"
set "ps_run=%ps_exe% "

setlocal EnableDelayedExpansion

set "error="
for %%i in ("net1", "net2") do (
    set "%%i="
    for /f "skip=3 tokens=1,* delims=: " %%j in ('%ps_exe% "netsh %%~i show global"') do (
        set "%%~i=!%%~i! %%k"
    )
)
set "net1=!net1:~1!"
set "net2=!net2:~1!"

:: Désactiver les services inutiles
echo Désactivation des services inutiles...
for %%s in (
    "XblAuthManager"
    "XblGameSave"
    "XboxNetApiSvc"
    "DiagTrack"
) do (
    echo Désactivation du service %%~s...
    %ps_run% "Set-Service -Name %%~s -StartupType Disabled"
)

:: Désactiver les tâches planifiées inutiles
echo Désactivation des tâches planifiées inutiles...
for %%t in (
    "\\Microsoft\\Windows\\Application Experience\\Microsoft Compatibility Appraiser"
    "\\Microsoft\\Windows\\Application Experience\\ProgramDataUpdater"
    "\\Microsoft\\Windows\\Autochk\\Proxy"
    "\\Microsoft\\Windows\\Customer Experience Improvement Program\\Consolidator"
    "\\Microsoft\\Windows\\Customer Experience Improvement Program\\KernelCeipTask"
    "\\Microsoft\\Windows\\Customer Experience Improvement Program\\UsbCeip"
) do (
    echo Désactivation de la tâche planifiée %%~t...
    %ps_run% "Schtasks /Change /TN \"%%~t\" /DISABLE"
)

echo Optimisation terminée.
pause