import os
import subprocess
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='patch_pioneer.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s:%(message)s')

def check_for_updates():
    """Check for available Windows updates using PowerShell."""
    try:
        logging.info("Checking for updates...")
        result = subprocess.run(
            ["powershell", "-Command", "Get-WindowsUpdate"],
            capture_output=True, text=True, check=True
        )
        updates = result.stdout
        logging.info("Updates found:\n%s", updates)
        return updates
    except subprocess.CalledProcessError as e:
        logging.error("Failed to check for updates: %s", e)
        return None

def install_updates():
    """Install available Windows updates."""
    try:
        logging.info("Installing updates...")
        subprocess.run(
            ["powershell", "-Command", "Install-WindowsUpdate -AcceptAll"],
            check=True
        )
        logging.info("Updates installed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error("Failed to install updates: %s", e)

def reboot_system():
    """Reboot the system if required."""
    try:
        logging.info("Rebooting system...")
        subprocess.run(["shutdown", "/r", "/t", "0"], check=True)
    except subprocess.CalledProcessError as e:
        logging.error("Failed to reboot system: %s", e)

def main():
    logging.info("PatchPioneer started.")
    
    updates = check_for_updates()
    if updates:
        install_updates()
        reboot_system()
    
    logging.info("PatchPioneer finished.")

if __name__ == "__main__":
    main()