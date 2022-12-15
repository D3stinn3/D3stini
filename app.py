print("Hello World!")
import os

"""Absolute Paths"""

# to abtain the absolute path of this particular python file

absolute_pat = os.path.abspath('.')
print(absolute_pat)

def absolute_assumption():
    path = absolute_pat
    base_name = os.path.basename(path)
    return base_name

experiment = absolute_assumption()
print(experiment)

# try manipulating the file path as you please

def resolute_path():
    path = absolute_pat
    split_paths = (absolute_pat, path)

    for item in split_paths:
        if item == path:
            print(item)
        break

experiment2 = resolute_path()
print(experiment2)

"""Lets Work on a file and try obtaining the path"""

def working_directories(manipulated):
    bacon_file = open('bacon.txt', 'w')
    bacon_file.write("Hello World!")
    bacon_file.close()

    with open('bacon.txt', 'r') as baconFile:
        lines = baconFile.read()
        line = manipulated.append(lines)
        return line

outp = working_directories([])
        

