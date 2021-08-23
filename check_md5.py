import os
import sys
import hashlib



files_md5 = {}
new_files_md5 = {}

def md5sum(path,files_md5_set):
    for i in os.listdir(path):
        md5 = hashlib.md5()
        file = os.path.join(path, i)
        if os.path.isfile(file):
            with open(file,mode='rb') as fd:
                while True:
                    data = fd.read(4096)
                    if data:
                        md5.update(data)
                    else:
                        file_modify = file[file.find("/"):]
                        files_md5_set[file_modify] = md5.hexdigest()
                        break
        else:
            md5sum(file,files_md5_set)

if __name__ == '__main__':
    md5sum(sys.argv[1],files_md5)
    md5sum(sys.argv[2],new_files_md5)
    set1 = set(files_md5.items())
    set2 = set(new_files_md5.items())
    for item in (set1 ^ set2):
        print(item,end='')
        print("\n")
