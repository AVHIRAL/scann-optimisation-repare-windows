import os
import subprocess

def run_powershell_cmd(cmd):
    completed_process = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)
    if completed_process.returncode != 0:
        print(f"Erreur lors de l'exécution de la commande: {cmd}")
        print(completed_process.stderr)
    else:
        print(completed_process.stdout)

# Désactiver les services inutiles
services_to_disable = [
    "XblAuthManager",
    "XblGameSave",
    "XboxNetApiSvc",
    "DiagTrack"
]

for service in services_to_disable:
    print(f"Désactivation du service {service}...")
    run_powershell_cmd(f"Set-Service -Name {service} -StartupType Disabled")

# Désactiver les tâches planifiées inutiles
tasks_to_disable = [
    "\\Microsoft\\Windows\\Application Experience\\Microsoft Compatibility Appraiser",
    "\\Microsoft\\Windows\\Application Experience\\ProgramDataUpdater",
    "\\Microsoft\\Windows\\Autochk\\Proxy",
    "\\Microsoft\\Windows\\Customer Experience Improvement Program\\Consolidator",
    "\\Microsoft\\Windows\\Customer Experience Improvement Program\\KernelCeipTask",
    "\\Microsoft\\Windows\\Customer Experience Improvement Program\\UsbCeip",
]

for task in tasks_to_disable:
    print(f"Désactivation de la tâche planifiée {task}...")
    run_powershell_cmd(f"Schtasks /Change /TN \"{task}\" /DISABLE")

print("Optimisation terminée.")