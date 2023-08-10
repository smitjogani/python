# capitalize all first letter of files which stores in testing folder
'''
import os


def removeFiles(filen):
    DND = open(filen)
    l = (DND.read())
    var = (l.split('\n'))
    DND.close()
    return var


def arry(pathn, filen, ext):
    filen = filen
    pathn = pathn
    os.chdir(pathn)
    count = 0
    var = removeFiles(filen)
    for f in os.listdir():
        f_name, f_ext = os.path.split(f)
        if f_ext == f'.{ext}':
            newName = f'{str(count)}{f_ext}'
            count += 1
            os.rename(f, newName)
            pass
        if f_name not in var:
            tn = f_name.title()
            new_name = f'{tn}{f_ext}'
        else:
            new_name = f'{new_name}{f_ext}'
        os.rename(f, new_name)


if __name__ == '__main__':
    pathn = input("Enter the path name : ")
    filen = input("Enter the name which contain Name of Files Not to alter :")
    ext = input("Enter the Extenction / Formate :")

    arry(pathn, filen, ext)
'''
import os


def soldier(path, file, formate):
    os.chdir(path)
    l = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())
        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}.{format}")
            i += 1


soldier(r"S:\Practicals\python\may\testing",
        r"S:\Practicals\python\may\may1.py", 
        ".jpg")

