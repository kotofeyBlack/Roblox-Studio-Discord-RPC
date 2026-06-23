# Roblox Studio Discord RPC

🚀 Display your Roblox Studio activity directly in Discord Rich Presence.

Roblox Studio Discord RPC automatically detects your currently opened Roblox Studio project and updates your Discord status in real time.

## Features

* 🎮 Discord Rich Presence integration
* 📁 Automatic project detection
* ⏱️ Session time tracking
* 🖥️ Lightweight background application
* ⚡ Fast and simple setup
* 🔄 Automatic status updates

## Preview

Discord Status:

Developing a Roblox Experience

Project: My Awesome Game

Elapsed Time: 2h 15m

## Installation

### Requirements

* Windows 10/11
* Discord Desktop
* Roblox Studio
* Python 3.10+

### Install Dependencies

```bash
pip install pypresence pywin32 psutil
```

### Run

```bash
python RobloxStudio.py
```

## Build EXE

```bash
pyinstaller --onefile --noconsole "Roblox Studio Discord RPC.py"
```

The executable will be generated in the `dist` folder.

## How It Works

The application detects Roblox Studio windows and automatically updates Discord Rich Presence with:

* Current project name
* Development status
* Session duration

## License

MIT License

## Author

Created by Kotofey Black.
