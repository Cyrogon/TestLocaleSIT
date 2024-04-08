import os
import subprocess
import yaml
from datetime import datetime

# Define an array with en inside since en will always build
langs = ["en"]

# Create a fucntion that makes a shorthand for the make command as well as setting OS vars
# before execution
def build_doc(version, language, tag):
    os.environ["current_version"] = version
    os.environ["current_language"] = language
    os.environ['SPHINXOPTS'] = "-D language='{}'".format(language)
    subprocess.run("TZ=UTC make html", shell=True)

os.environ["build_all_docs"] = str(True)
os.environ["pages_root"] = "https://cyrogon.github.io/TestLocaleSIT"

# Create a shorthand for making and moving a directory
def move_dir(src, dst):
  subprocess.run(["mkdir", "-p", dst])
  subprocess.run("mv "+src+'* ' + dst, shell=True)

# List all Langs in the Locales folder for building
langs += os.listdir("locales")

# Iterate over all found languages and build then move each one to it's designated dir
for i in langs:
   build_doc("latest", i, "py-rewrite")
   move_dir("./build/html/", "../pages/{}".format(i))

# reading the yaml file
with open("versions.yaml", "r") as yaml_file:
  docs = yaml.safe_load(yaml_file)

# and looping over all values to call our build with version, language and its tag
for version, details in docs.items():
  tag = details.get('tag', '')
  for language in details.get('languages', []): 
    build_doc(version, language, version)
    move_dir("./build/html/", "../pages/"+version+'/'+language+'/')