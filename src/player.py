# mimi is a nice cat 

# github : https://github.com/MohssineX

# Copyright (C) 2026 Mohssine <https://github.com/MohssineX>

# player.py

import config as cfg
from config import COLOR_RED, COLOR_YELLOW, COLOR_RESET

import urllib.request
import miniaudio


def play_surah(url, Nsurahint):

    class MP3Source(miniaudio.StreamableSource):

        def __init__(self, url):
            self.response = urllib.request.urlopen(
                url,
                timeout=cfg.timeoutCfg
            )
            self.error_occurred = False

        def read(self, num_bytes):
            try:
                return self.response.read(num_bytes)

            except Exception:
                if not self.error_occurred:
                    print("")
                    print("")
                    print(
                        f"{COLOR_RED}"
                        f"Err203 : Unexpected disconnection "
                        f"[Please restart {cfg.appName}]"
                        f"{COLOR_RESET}",
                        flush=True
                    )

                self.error_occurred = True
                return b""

    source = MP3Source(
        f"{url}{Nsurahint}.mp3"
    )

    stream = miniaudio.stream_any(
        source,
        miniaudio.FileFormat.MP3
    )

    device = miniaudio.PlaybackDevice()

    device.start(stream)

    print("The Quran is playing")
    print("")

    print(
        f"{COLOR_YELLOW}"
        "Thank you for using TilawaPlayer!"
        f"{COLOR_RESET}"
    )

    print("")

    return device

