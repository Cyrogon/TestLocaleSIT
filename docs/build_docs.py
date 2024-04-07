# a single build step, which keeps conf.py and versions.yaml at the main branch
# in generall we use environment variables to pass values to conf.py, see below
# and runs the build as we did locally
import os
import subprocess
import yaml
def build_doc(version, language, tag):
    os.environ["current_version"] = version
    os.environ["current_language"] = language
    subprocess.run("git checkout " + tag, shell=True)
    subprocess.run("git checkout main -- conf.py", shell=True)
    subprocess.run("git checkout main -- versions.yaml", shell=True)
    os.environ['SPHINXOPTS'] = "-D language='{}'".format(language)
    subprocess.run("make html", shell=True)    

# a move dir method because we run multiple builds and bring the html folders to a 
# location which we then push to github pages
def move_dir(src, dst):
  subprocess.run(["mkdir", "-p", dst])
  subprocess.run("mv "+src+'* ' + dst, shell=True)

# to separate a single local build from all builds we have a flag, see conf.py
os.environ["build_all_docs"] = str(True)
os.environ["pages_root"] = "https://cyrogon.github.io/TestLocaleSIT"

# manually the main branch build in the current supported languages
build_doc("latest", "en", "main")
move_dir("./build/html/", "../pages/en/")
build_doc("latest", "de", "main")
move_dir("./build/html/", "../pages/de/")
build_doc("latest", "zh_cn", "main")
move_dir("./build/html/", "../pages/zh_cn/")
build_doc("latest", "fr", "main")
move_dir("./build/html/", "../pages/fr/")
build_doc("latest", "es", "main")
move_dir("./build/html/", "../pages/es/")

# reading the yaml file
with open("versions.yaml", "r") as yaml_file:
  docs = yaml.safe_load(yaml_file)

# and looping over all values to call our build with version, language and its tag
for version, details in docs.items():
  tag = details.get('tag', '')
  for language in details.get('languages', []): 
    build_doc(version, language, version)
    move_dir("./build/html/", "../pages/"+version+'/'+language+'/')