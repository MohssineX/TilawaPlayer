# mimi is a nice cat 

# github : https://github.com/MohssineX

# Copyright (C) 2026 Mohssine <https://github.com/MohssineX>

# downloader.py

import os
import config as cfg
import urllib.request
from config import COLOR_YELLOW, COLOR_GREEN, COLOR_RESET

def download_surah(url, reciter, Nsurahint):
    file_path = os.path.join(os.getcwd(), f"TilawaPlayerR{reciter}S{Nsurahint}.mp3")

    print("An audio file is being downloaded...")

    with urllib.request.urlopen(f"{url}{Nsurahint}.mp3", timeout=cfg.timeoutCfg) as response:

        with open(file_path, "wb") as file:
            while True:
                chunk = response.read(cfg.chunkDownload)

                if not chunk:
                    break

                file.write(chunk)

    print("")
    print(f"{COLOR_YELLOW}A file was downloaded to {file_path}{COLOR_RESET}")
    print("")
    print(f"{COLOR_YELLOW}Thank you for using TilawaPlayer!{COLOR_RESET}")
    print("")

    user_action = input(f"{COLOR_GREEN}Type 'r' to restart or 'q' to quit : {COLOR_RESET}")
    return user_action
