import sys
import subprocess

def create_wordpress_site(site_name):
    try:
        subprocess.check_call(['wp', 'core', 'download', '--version=latest'])
        subprocess.check_call(['wp', 'config', 'create', '--dbname=wordpress', '--dbuser=root', '--dbpass=pass'])
        subprocess.check_call(['wp', 'core', 'install', '--url=http://localhost/' + site_name, '--title=' + site_name, '--admin_user=admin', '--admin_password=admin', '--admin_email=admin@example.com'])
        print(f"WordPress site '{site_name}' created successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while creating the WordPress site: {e}")
        sys.exit(1)

if len(sys.argv) != 2:
    print("Please provide the site name as a command-line argument.")
    sys.exit(1)

site_name = sys.argv[1]
create_wordpress_site(site_name)
