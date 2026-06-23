# Roblox Studio Discord RPC

A lightweight Discord Rich Presence application for Roblox Studio.

This project automatically updates your Discord status while developing in Roblox Studio, displaying the currently opened project and development session time.

## Features

* 🎮 Discord Rich Presence integration
* 📁 Automatically detects the current Roblox Studio project
* ⏱️ Tracks development session time
* 🚀 Lightweight and easy to use
* 🔄 Automatic status updates
* 🖥️ Runs in the background

## Requirements

* Windows
* Python 3.10+
* Discord Desktop App
* Roblox Studio

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourname/Roblox-Studio-Discord-RPC.git
```

2. Install dependencies:

```bash
pip install pypresence pywin32 psutil
```

3. Run the application:

```bash
python RobloxStudio.py
```

## Build EXE

```bash
pyinstaller --onefile --noconsole RobloxStudio.py
```

The executable will be created in the `dist` folder.

## Discord Status Example

Developing a Roblox Experience

Project: My Awesome Game

Elapsed Time: 1h 24m

## License

MIT License
