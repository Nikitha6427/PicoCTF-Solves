import os

def unzipAll():
    for i in range(1000, 0, -1):
        os.system(f"tar -xvf {i}.tar")
        if i != 1000:
            os.system(f"rm {i}.tar")

unzipAll()
