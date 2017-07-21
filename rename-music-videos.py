import os
import re

home = "L:\Videos\Music"

pattern = r'\s-\s'

new_folder_list = []

files = [f for f in os.listdir(home) if os.path.isfile(os.path.join(home, f))]
for file in files:
    new_folder = file[0:re.search(pattern, file).start()]
    if not os.path.isdir(os.path.join(home, new_folder)):
        print("Making new directory named", "'" + new_folder + "'")
        os.makedirs(os.path.join(home, new_folder))
    print("Moving file", "'" + file + "'", "from", "'" + home + "'", "to", "'" + new_folder + "'")
    os.rename(os.path.join(home, file), os.path.join(home, new_folder, file))

