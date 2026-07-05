import time

import psutil
import win32gui
from pypresence import Presence

CLIENT_ID = "1516783637633306645"
UPDATE_INTERVAL = 10


def connect_rpc():
    while True:
        try:
            client = Presence(CLIENT_ID)
            client.connect()
            return client
        except Exception:
            time.sleep(5)


def is_roblox_studio_running():
    for proc in psutil.process_iter(["name"]):
        try:
            name = proc.info["name"]
            if name and name.lower() == "robloxstudiobeta.exe":
                return True
        except Exception:
            pass
    return False


def get_project_name():
    windows = []

    def enum_handler(hwnd, _):
        if not win32gui.IsWindowVisible(hwnd):
            return

        title = win32gui.GetWindowText(hwnd)
        if title == "Roblox Studio" or title.endswith(" - Roblox Studio"):
            windows.append(title)

    win32gui.EnumWindows(enum_handler, None)

    for title in windows:
        if title == "Roblox Studio":
            return "IDLE_MENU"

        if title.endswith(" - Roblox Studio"):
            raw_title = title.replace(" - Roblox Studio", "").strip()
            return raw_title.split(" - ")[0].strip()

    return None


rpc = connect_rpc()
current_project = ""
start_time = int(time.time())
presence_visible = False


while True:
    try:
        if not is_roblox_studio_running():
            if presence_visible:
                try:
                    rpc.clear()
                except Exception:
                    rpc = connect_rpc()
                presence_visible = False

            current_project = ""
            start_time = int(time.time())
            time.sleep(UPDATE_INTERVAL)
            continue

        project = get_project_name()

        if project == "IDLE_MENU":
            rpc.update(
                details="Roblox Studio",
                state="Browsing Projects",
                large_image="robloxstudio",
                large_text="Roblox Studio",
            )
            current_project = ""
            start_time = int(time.time())
            presence_visible = True

        elif project:
            if project != current_project:
                current_project = project
                start_time = int(time.time())

            rpc.update(
                details="Developing a Roblox Experience",
                state=current_project,
                large_image="robloxstudio",
                large_text="Roblox Studio",
                start=start_time,
            )
            presence_visible = True

        else:
            rpc.update(
                details="Roblox Studio",
                state="Loading...",
                large_image="robloxstudio",
                large_text="Roblox Studio",
            )
            presence_visible = True

        time.sleep(UPDATE_INTERVAL)

    except Exception:
        try:
            rpc = connect_rpc()
        except Exception:
            pass
        time.sleep(UPDATE_INTERVAL)
