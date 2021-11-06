import zipfile
import os
import time
from os import listdir
from os.path import isfile, join

input_mods = input("Paste Packed Mods Dir here: ")
input_assets = input("Paste Packed Assets Dir here: ")
input_mods_game = input("Paste Game Mods Dir here: ")
input_assets_game = input("Paste Game Assets Dir here: ")

file_list_mods = os.listdir(input_mods)
file_list_assets = os.listdir(input_assets)


for first_file_mods in file_list_mods:
    print(f"File: {first_file_mods} found!")
    with zipfile.ZipFile(input_mods + str(first_file_mods),"r") as zip_ref:
        file_locaton_mods = str(first_file_mods).replace(".zip", "")
        onlyfiles = [f for f in listdir(file_locaton_mods) if isfile(join(file_locaton_mods, f))]
        while True:
            if ".dll" in onlyfiles[0]:
                print("success!")
                break
            else:
                onlyfiles.pop(0)

        dll_file = str(onlyfiles[0])

        dll_file_name = dll_file.replace(".dll", "")
        zip_ref.extractall(input_mods_game + dll_file_name)

print("Mod Copy Done \n Starting Assets Copy in 3 Seconds!")
time.sleep(3)

for first_file_assets in file_list_assets:
    print(f"File: {first_file_assets} found!")
    with zipfile.ZipFile(input_assets + str(first_file_assets),"r") as zip_ref:
        file_location_assets = str(first_file_assets).replace(".zip", "")
        onlyfiles = [f for f in listdir(file_location_assets) if isfile(join(file_location_assets, f))]
        while True:
            if ".dll" in onlyfiles[0]:
                print("success!")
                break
            else:
                onlyfiles.pop(0)

        dll_file = str(onlyfiles[0])

        dll_file_name = dll_file.replace(".dll", "")
        zip_ref.extractall(input_assets_game + dll_file_name)

print("Mods/Assets Install Finished!")
input("Press ENTER to EXIT")
