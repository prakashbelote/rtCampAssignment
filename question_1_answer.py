import sys
import subprocess

def verify_package(package_name):
    try:
        subprocess.check_output([package_name, '--version'])
        return True
    except OSError as e:
        return False

def install_package(package_name):
    try:
        subprocess.check_call(['sudo', 'apt', 'install', '-y', package_name])
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing {package_name}: {e}")
        sys.exit(1)

if not verify_package('docker'):
    print("Docker is not installed.")
    install_package('docker')
    print("Docker has been successfully installed!")

if not verify_package('docker-compose'):
    print("Docker Compose is not installed.")
    install_package('docker-compose')
    print("Docker Compose has been successfully installed!")
