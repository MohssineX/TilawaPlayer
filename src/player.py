# mimi is a nice cat 

# github : https://github.com/MohssineX

# Copyright (C) 2026 Mohssine <https://github.com/MohssineX>

# player.py

import config as cfg
from config import COLOR_GREEN, COLOR_RED, COLOR_YELLOW, COLOR_RESET
import urllib.request

import miniaudio

def play_surah(url, Nsurahint):

    class MP3Source(miniaudio.StreamableSource):

        def __init__(self, url):
            self.response = urllib.request.urlopen(url, timeout=cfg.timeoutCfg)
            self.error_occurred = False

        def read(self, num_bytes):
            try:
                return self.response.read(num_bytes)

            except Exception:
                if not self.error_occurred:
                    print("")
                    print("")
                    print(f"{COLOR_RED}Err203 : Unexpected disconnection [Please restart {cfg.appName}]{COLOR_RESET}", flush=True)
                    print("")
                    print(f"{COLOR_GREEN}Type 'r' to restart or 'q' to quit : {COLOR_RESET}", end="", flush=True)

                self.error_occurred = True
                return b""
                
    source = MP3Source(f"{url}{Nsurahint}.mp3")
    stream = miniaudio.stream_any(source, miniaudio.FileFormat.MP3)

    with miniaudio.PlaybackDevice() as device:
        device.start(stream)

        print("The Quran is playing")
        print("")

        print(f"{COLOR_YELLOW}Thank you for using TilawaPlayer!{COLOR_RESET}")
        print("")

        while True:
            user_action = input(
                f"{COLOR_GREEN}Type 'r' to restart or 'q' to quit : {COLOR_RESET}"
            ).lower().strip()

            if user_action in ("r", "q"):
                return user_action

            print(
                f"{COLOR_RED}Invalid option. Please type 'r' or 'q'.{COLOR_RESET}"
            )
