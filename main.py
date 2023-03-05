# coding: utf-8
import os
import keyboard
import time
import split
import re
import filecmp
import wmi
import socket
from zipfile import ZipFile
import shutil
import itertools
import threading
import time
import sys
from difflib import Differ
import requests

repo = []
run = True
username = os.getlogin()
inp3 = ""

os.chdir("C:\\Users\\" + str(username) + "\\desktop")


used_command = [""]
var_int = 0


def start_service(svc):
    os.system(f'net start {svc}')

def stop_service(svc):
    os.system(f'net stop {svc}')


while run:
    # get the path
    testingvar = os.getcwd()
    hi = " "
    i3 = ["", "", ""]
    inp = input(testingvar + "> ").lower()
    used_command.append(inp)
    s2 = inp
    if hi in s2:
        i3 = s2.split(" ")
        inp1 = i3[0]
        inp2 = i3[1]
        if inp1 == "cmp" or inp1 == "diff" or inp1 == "service":
            inp3 = i3[2]
    else:
        inp1 = inp


    if inp1 == "cd" and inp2 != "":
        try:
            os.chdir(str(inp2))
        except FileNotFoundError:
            print("Désolé le chemin d'accès n'existe pas")


    if inp1 == "exit":
        run = False

    if inp1 == "cls":
        # IDK how to do a real clean
        print("\n"*1000)

    if inp1 == "ls":
        Cdirectory = os.listdir()
        print(Cdirectory)

    if inp1 == "get":
        print(used_command)

    if inp1 == "m":
        print(used_command)

    if inp1 == "touch" and inp2 != "":
        Cfile = open(inp2, "w+")
        Cfile.close()

    if inp1 == "cat" and inp2 != "":
        try:
            Cfile = open(inp2, "r")
            res = Cfile.read()
            print(res)
            Cfile.close()
        except FileNotFoundError:
            print("Désolé le chemin d'accès n'existe pas")

    if inp1 == "ifconfig":

        # getting the hostname by socket.gethostname() method
        hostname = socket.gethostname()
        # getting the IP address using socket.gethostbyname() method
        ip_address = socket.gethostbyname(hostname)
        # printing the hostname and ip_address
        print(f"Hostname: {hostname}")
        print(f"IP Address: {ip_address}")

    if inp1 == "cmp" and inp2 != "" and inp3 != "":
        try:
            result = filecmp.cmp(inp2, inp3,)
            print(result)
        except FileNotFoundError:
            print("Désolé le chemin d'accès n'existe pas")

    if inp1 == "diff" and inp2 != "" and inp3 != "":
        try:
            with open(inp2) as file_1, open(inp3) as file_2:
                differ = Differ()

                for line in differ.compare(file_1.readlines(), file_2.readlines()):
                    print(line)
        except FileNotFoundError:
            print("Désolé le chemin d'accès n'existe pas")

    if inp1 == "ps":

        # Initializing the wmi constructor
        f = wmi.WMI()

        # Printing the header for the later columns
        print("pid   Process name")

        # Iterating through all the running processes
        for process in f.Win32_Process():
            # Displaying the P_ID and P_Name of the process
            print(f"{process.ProcessId:<10} {process.Name}")

    '''if inp1 == "zip" and inp2 != "" and inp3 == "":
        try:
            if inp3 == "":
                inp3 = inp2
            shutil.make_archive(inp3, 'zip', inp2)
        except PermissionError:
            print("Désolé vous n'avez pas la permission")'''

    if inp1 == "zip" and inp2 != "":
        try:
            zip_path = testingvar + "\\zip_file.zip"
            # Create object of ZipFile
            with ZipFile("zip_file.zip", 'w') as zip_object:
                # Traverse all files in directory
                for folder_name, sub_folders, file_names in os.walk(inp2):
                    for filename in file_names:
                        # Create filepath of files in directory
                        file_path = os.path.join(folder_name, filename)
                        # Add files to zip file
                        zip_object.write(file_path, os.path.basename(file_path))

            if os.path.exists("zip_file.zip"):
                print("ZIP file created at " + zip_path)
            else:
                print("ZIP file not created")
        except PermissionError:
            print("Désolé vous n'avez pas la permission")

    if inp1 == "unzip" and inp2 != "" and inp3 == "":
        if inp3 == "":
            inp3 = testingvar
            done = False

    if inp1 == "unzip" and inp2 != "" and inp3 != "":
        try:
            shutil.unpack_archive(inp2, inp3)
        except FileNotFoundError:
            print("Désolé le chemin d'accès n'existe pas")

    if inp1 == "diskusage":
        var = shutil.disk_usage(testingvar)
        print(var)


    if inp1 == "echo" and inp2 != "":
        print(inp2)

    if inp1 == "service" and inp2 != "" and inp3 != "":
        if inp3 == "-s":
            start_service(inp2)

        if inp3 == "-k":
            stop_service(inp2)


    if inp1 == "whoami":
        print(username)

    if inp1 == "search" and inp2 != "":
        try:
            done = False
            res = []

            # here is the animation
            def animate():
                for c in itertools.cycle(['|', '/', '-', '\\']):
                    if done:
                        break
                    sys.stdout.write('\rloading ' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                    sys.stdout.write()



            t = threading.Thread(target=animate)
            t.start()

            # long process here
            for (dir_path, dir_names, file_names) in os.walk(testingvar):
                res.extend(file_names)

            if inp2 in res:
                print("file found at : " + os.path.abspath(inp2))
            done = True


        except FileNotFoundError:
            print("Désolé le chemin d'accès n'existe pas")

    if inp1 == "wget" and inp2 != "":
        url = inp2
        r = requests.get(url, allow_redirects=True)

        open('facebook.ico', 'wb').write(r.content)