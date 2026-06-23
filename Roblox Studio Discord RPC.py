import time
import win32gui
import psutil
from pypresence import Presence

CLIENT_ID = "1516783637633306645"

rpc = Presence(CLIENT_ID)
rpc.connect()

current_project = ""
start_time = int(time.time())


def is_roblox_studio_running():
    for proc in psutil.process_iter(["name"]):
        try:
            if proc.info["name"] and proc.info["name"].lower() == "robloxstudiobeta.exe":
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

        if title.endswith(" - Roblox Studio"):
            windows.append(title)

    win32gui.EnumWindows(enum_handler, None)

    for title in windows:
        project = title.replace(" - Roblox Studio", "").strip()

        if project:
            return project

    return None


while True:
    try:
        if not is_roblox_studio_running():
            rpc.update(
                details="Roblox Studio",
                state="Not Open"
            )
            time.sleep(10)
            continue

        project = get_project_name()

        if project:
            if project != current_project:
                current_project = project
                start_time = int(time.time())

            rpc.update(
                details="Developing a Roblox Experience",
                state=current_project,
                large_image="robloxstudio",
                large_text="Roblox Studio",
                start=start_time
            )
        else:
            rpc.update(
                details="Roblox Studio",
                state="Editing Project",
                large_image="robloxstudio",
                large_text="Roblox Studio"
            )

        time.sleep(10)

    except Exception:
        time.sleep(10)