import glob

path = 'D:\\bca\\Practicals\\practicals\\python\\collage\\ch4'

files = [f for f in glob.glob(path + "**/*.py", recursive = True)]
for f in files:
    print(f)