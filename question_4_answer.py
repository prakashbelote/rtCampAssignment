import sys
import subprocess

def add_hosts_entry(site_name):
    hosts_entry = "127.0.0.1   " + site_name + "\n"
    try:
        with open('/etc/hosts', 'a') as hosts_file:
            hosts_file.write(hosts_entry)
        print(f"Added /etc/hosts entry for '{site_name}' successfully!")
    except IOError as e:
        print(f"Error occurred while adding /etc/hosts entry: {e}")
        sys.exit(1)

if len(sys.argv) != 2:
    print("Please provide the site name as a command-line argument.")
    sys.exit(1)

site_name = sys.argv[1]
add_hosts_entry(site_name)
