import fileinput
import argparse 
import subprocess 
parser = argparse.ArgumentParser(description='Process some arguments.')
parser.add_argument('--description', dest='description',
                    help='The description for your package.')

args = parser.parse_args()
description = args.description
if not description:
    description = "A reusable Django application using the Krypted Gaming template."
    
# Build Variables
get_package_name = subprocess.run(
    ['basename `git rev-parse --show-toplevel`'], 
    stdout=subprocess.PIPE, 
    shell=True)

get_package_author = subprocess.run(
    ['git config user.name'],
    stdout=subprocess.PIPE,
    shell=True)

get_package_email = subprocess.run(
    ['git config user.email'],
    stdout=subprocess.PIPE,
    shell=True)

get_package_url = subprocess.run(
    ['git remote get-url origin'],
    stdout=subprocess.PIPE,
    shell=True)

package_name=get_package_name.stdout.decode('utf-8').strip()
app_name = package_name.replace("-", "_")
title = app_name.title().replace("_", " ")
config_name = ''.join(x for x in app_name.title() if x != '_')
package_author = get_package_author.stdout.decode('utf-8').strip()
package_email = get_package_email.stdout.decode('utf-8').strip()
package_url = get_package_url.stdout.decode('utf-8').strip()

# Create Application
create_project = subprocess.run(
    [f"django-admin startapp {app_name}"],
    stdout=subprocess.PIPE,
    shell=True)

# Build Files

init_py = (
    f"__title__ = '{title}'" + "\n"
    f"__description__ = '{description}'" + "\n"
    f"__package_name__ = '{package_name}'" + "\n"
    f"__github_url__ = '{package_url}'" + "\n"
    f"__version__ = '0.0.1'" + "\n"
    f"__author__ = '{package_author}'" + "\n"
    f"__author_email__ = '{package_email}'" + "\n"
    f"__license__ = 'MIT License'" + "\n"
    f"__copyright__ = f\"Copyright © 2017-2020 {package_author}. All rights reserved.\"" + "\n"
    f"default_app_config = \"{app_name}.apps.{config_name}Config\"" + "\n"
)

with fileinput.FileInput("./setup.py", inplace=True) as file:
    for line in file:
        print(line.replace('unknown_app', app_name), end='')

with fileinput.FileInput("./.travis.yml", inplace=True) as file:
    for line in file:
        print(line.replace('django_package_template', app_name), end='')

with fileinput.FileInput("./conf/settings.py", inplace=True) as file:
    for line in file:
        print(line.replace('django_package_template', app_name), end='')

f = open(f"{app_name}/__init__.py", "a+")
f.write(init_py)

