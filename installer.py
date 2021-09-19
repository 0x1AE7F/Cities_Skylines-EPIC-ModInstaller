import zipfile
import os
import time

input_mods = input("Paste Packed Mods Dir here: ")
input_assets = input("Paste Packed Assets Dir here: ")
input_mods_game = input("Paste Game Mods Dir here: ")
input_assets_game = input("Paste Game Assets Dir here: ")

file_list_mods = os.listdir(input_mods)
file_list_assets = os.listdir(input_assets)


for file_one_mods in file_list_mods:
    print(f"File: {file_one_mods} found!")
    with zipfile.ZipFile(input_mods + str(file_one_mods),"r") as zip_ref:
        file_one_mods = str(file_one_mods).replace(".zip", "")
        zip_ref.extractall(input_mods_game + file_one_mods)

print("Mod Copy Done \n Starting Assets Copy in 3 Seconds!")
time.sleep(3)

for file_one_assets in file_list_assets:
    print(f"File: {file_one_assets} found!")
    with zipfile.ZipFile(input_assets + str(file_one_assets),"r") as zip_ref:
        file_one_assets = str(file_one_assets).replace(".zip", "")
        zip_ref.extractall(input_assets_game + file_one_assets)

print("Mods/Assets Install Finished!")
input("Press ENTER to EXIT")
