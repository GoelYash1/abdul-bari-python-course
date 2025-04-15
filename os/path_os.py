import os.path

# path.exists check if path exists
print(os.path.exists('C:\\MyPython'))
print(os.path.exists('C:'))

# path.isfile check if the path points to a file
print(os.path.isfile(r'C:\Users\yagoel\PycharmProjects\abdul-bari-python-course\notes'))

# path.isdir check if the path points to a directory
print(os.path.isdir('C:'))

print(os.path.abspath('path_os.py'))
print(os.path.relpath(r'C:\Users\yagoel\PycharmProjects\abdul-bari-python-course\os\path_os.py'))
"""
    path.split() splits the path to a tuple of two entries with last part of the path as a different entry a/b/c => a/b, c
    path.join() is used to join
    path.basename() gives the last name i.e a/b/c c
    path.dirname() gives the directory name before that i.e a/b/c a/b
    path.getmtime() gives modified time of a file
    path.getatime() gives access time of a file
    path.getatime() gives access time of a file
"""