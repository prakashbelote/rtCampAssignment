import sys
import subprocess
import shutil
import webbrowser

def add_hosts_entry(site_name):
    hosts_entry = "127.0.0.1   " + site_name + "\n"
    try:
        with open('/etc/hosts', 'a') as hosts_file:
            hosts_file.write(hosts_entry)
        print(f"Added /etc/hosts entry for '{site_name}' successfully!")
    except IOError as e:
        print(f"Error occurred while adding /etc/hosts entry: {e}")
        sys.exit(1)

def open_site_in_browser(site_name):
    try:
        webbrowser.open("http://" + site_name)
    except webbrowser.Error as e:
        print(f"Error occurred while opening '{site_name}' in the browser: {e}")

def enable_site():
    try:
        subprocess.check_call(['docker-compose', 'up', '-d'])
        print("Site enabled successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while enabling the site: {e}")
        sys.exit(1)

def disable_site():
    try:
        subprocess.check_call(['docker-compose', 'down'])
        print("Site disabled successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while disabling the site: {e}")
        sys.exit(1)

def delete_site():
    try:
        subprocess.check_call(['docker-compose', 'down', '-v'])
        shutil.rmtree('nginx')
        shutil.rmtree('php')
        shutil.rmtree('mysql')
        print("Site deleted successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while deleting the site: {e}")
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"Error occurred while deleting the site: {e}")
        sys.exit(1)

if len(sys.argv) < 3:
    print("Please provide the site name and subcommand as command-line arguments.")
    sys.exit(1)

site_name = sys.argv[1]
subcommand = sys.argv[2]

if subcommand == 'enable':
    add_hosts_entry(site_name)
    enable_site()
    open_site_in_browser(site_name)
elif subcommand == 'disable':
    disable_site()
elif subcommand == 'delete':
    delete_site()
else:
    print("Invalid subcommand. Please use 'enable', 'disable', or 'delete'.")
    sys.exit(1)
