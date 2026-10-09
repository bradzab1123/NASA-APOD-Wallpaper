# NASA APOD Wallpaper

Automatically downloads NASA's **Astronomy Picture of the Day (APOD)** and sets it as your desktop wallpaper on **Windows** or **macOS**. Run it once by hand, or schedule it to run every day so you get a new space picture each morning.

---

## Table of Contents

- [What It Does](#what-it-does)
- [Requirements](#requirements)
- [Quick Start (for people comfortable with Python)](#quick-start-for-people-comfortable-with-python)
- [Step-by-Step Setup (for everyone else)](#step-by-step-setup-for-everyone-else)
- [Run It Automatically Every Day](#run-it-automatically-every-day)
- [Where Things Are Saved](#where-things-are-saved)
- [Troubleshooting](#troubleshooting)
- [Known Limitations](#known-limitations)
- [Project Structure](#project-structure)
- [Uninstalling](#uninstalling)
- [Image Credits and Usage](#image-credits-and-usage)
- [License](#license)

---

## What It Does

1. Asks NASA's APOD feed (`science.nasa.gov`) for the most recent post.
2. If that post is a **video** instead of an image, the script stops and leaves your wallpaper alone.
3. If it's an **image**, it downloads the high-resolution version to `Pictures/APOD/apod-YYYY-MM-DD.jpg` in your user folder.
4. Sets that image as your desktop wallpaper:
   - **Windows:** through the built-in Windows API.
   - **macOS:** through a small AppleScript that tells *System Events* to change the desktop picture.

---

## Requirements

| Requirement | Windows | macOS |
|---|---|---|
| Operating system | Windows 10 or 11 | A recent version of macOS |
| Python | 3.9 or newer | 3.9 or newer |
| Internet connection | Yes | Yes |
| Python packages | `requests` | `requests` |

**No NASA account or API key is needed.** The script reads NASA's public APOD feed directly.

**One `requirements.txt` covers both Windows and macOS.** The only extra package the script needs is `requests`. Everything else it uses (`os`, `sys`, `platform`, `subprocess`, `ctypes`) comes built into Python.

---

## Quick Start (for people comfortable with Python)

```bash
git clone https://github.com/bradzab1123/NASA-APOD-Wallpaper.git
cd NASA-APOD-Wallpaper
python -m venv .venv          # macOS: python3 -m venv .venv

# Install packages
.venv\Scripts\python.exe -m pip install -r requirements.txt   # Windows
.venv/bin/python -m pip install -r requirements.txt           # macOS

# Run
.venv\Scripts\python.exe NasaWallpaper.py    # Windows
.venv/bin/python NasaWallpaper.py            # macOS
```

---

## Step-by-Step Setup (for everyone else)

> **Tip:** These steps put the project in your **home folder** (for example `C:\Users\Jane\NASA-APOD-Wallpaper` or `/Users/jane/NASA-APOD-Wallpaper`). Avoid putting it in Documents, Desktop, or Downloads. On macOS those folders are privacy-protected and will block the daily scheduled run. On Windows, Documents is often synced by OneDrive, which can cause odd problems.

### Step 1: Install Python

<details>
<summary><b>Windows</b></summary>

1. Go to <https://www.python.org/downloads/> and click the big **Download Python** button.
2. Run the installer.
3. **Important:** on the first screen, check the box that says **"Add python.exe to PATH"**, then click **Install Now**.
4. When it finishes, open **PowerShell** (press Start, type `PowerShell`, press Enter) and run:
   ```powershell
   python --version
   ```
   You should see something like `Python 3.13.x`.

If typing `python` opens the Microsoft Store instead, either re-run the installer and make sure the PATH box is checked, or use `py` in place of `python` in the commands below.
</details>

<details>
<summary><b>macOS</b></summary>

1. Go to <https://www.python.org/downloads/> and download the macOS installer.
2. Open the downloaded `.pkg` file and click through the installer.
3. Open **Terminal** (press `Cmd + Space`, type `Terminal`, press Enter) and run:
   ```bash
   python3 --version
   ```
   You should see something like `Python 3.13.x`.

On macOS, always type `python3`, not `python`.
</details>

### Step 2: Download This Project

**Option A: Download a ZIP (easiest)**

1. On this GitHub page, click the green **Code** button, then **Download ZIP**.
2. Extract the ZIP into your home folder.
3. GitHub names the extracted folder `NASA-APOD-Wallpaper-main`. **Rename it to `NASA-APOD-Wallpaper`** so the commands below match.

**Option B: Use Git**

```bash
cd ~
git clone https://github.com/bradzab1123/NASA-APOD-Wallpaper.git
```

(On macOS, if you've never used Git before, the Mac will offer to install "Command Line Tools." Click **Install**.)

### Step 3: Create a Virtual Environment and Install Packages

A *virtual environment* (`.venv`) is a private copy of Python just for this project, so the packages you install here don't affect anything else on your computer.

**Windows (PowerShell):**
```powershell
cd $HOME\NASA-APOD-Wallpaper
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**macOS (Terminal):**
```bash
cd ~/NASA-APOD-Wallpaper
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

> These instructions call the virtual environment's Python directly (`.venv\Scripts\python.exe` or `.venv/bin/python`) instead of "activating" it. Activating isn't needed, and skipping it avoids the common PowerShell "running scripts is disabled on this system" error.

### Step 4: Run It

**Windows:**
```powershell
.venv\Scripts\python.exe NasaWallpaper.py
```

**macOS:**
```bash
.venv/bin/python NasaWallpaper.py
```

If it works, you'll see output like this and your wallpaper will change:

```
APOD is an image. Storing URL
C:\Users\Jane\Pictures\APOD\apod-2026-10-07.jpg
OS is Windows
Successfully set wallpaper!
```

**macOS first run:** a pop-up will say something like *"Terminal wants access to control System Events."* Click **OK**. That permission is what lets the script change your wallpaper. If you clicked **Don't Allow** by mistake, go to **System Settings → Privacy & Security → Automation → Terminal** and turn on **System Events**.

---

## Run It Automatically Every Day

### Windows: Task Scheduler

1. Press Start, type **Task Scheduler**, and open it.
2. In the right-hand panel, click **Create Basic Task…**
3. **Name:** `NASA APOD Wallpaper`. Click **Next**.
4. **Trigger:** choose **Daily**. Click **Next**, pick a time (for example 9:00 AM), and click **Next**.
5. **Action:** choose **Start a program**. Click **Next**.
6. Fill in the three boxes, replacing `YOUR_USERNAME` with your Windows username:

   | Box | Value |
   |---|---|
   | Program/script | `C:\Users\YOUR_USERNAME\NASA-APOD-Wallpaper\.venv\Scripts\pythonw.exe` |
   | Add arguments | `NasaWallpaper.py` |
   | Start in | `C:\Users\YOUR_USERNAME\NASA-APOD-Wallpaper` |

   (`pythonw.exe` is the same as `python.exe`, except it doesn't flash a black console window.)
7. Click **Next**, then **Finish**.
8. **Test it:** find the task in the list, right-click it, and choose **Run**.

**Optional improvements:** right-click the task, choose **Properties**, and then:
- On the **Triggers** tab, click **New…** and add **At log on**, so it also runs when you sign in.
- On the **Settings** tab, check **Run task as soon as possible after a scheduled start is missed**, so it catches up if your PC was off at the scheduled time.

Leave **"Run only when user is logged on"** selected (it's the default). The wallpaper belongs to your signed-in session, so the task must run as you.

### macOS: launchd

macOS uses *launch agents* for scheduled jobs.

1. Find your username:
   ```bash
   whoami
   ```
2. Create the launch agent file:
   ```bash
   mkdir -p ~/Library/LaunchAgents
   open -e ~/Library/LaunchAgents/com.apod.wallpaper.plist
   ```
   If TextEdit says the file doesn't exist, run `touch ~/Library/LaunchAgents/com.apod.wallpaper.plist` first, then the `open -e` command again.
3. Paste the following, replacing **both** `YOUR_USERNAME` entries with the name from step 1, and save:

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>Label</key>
       <string>com.apod.wallpaper</string>

       <key>ProgramArguments</key>
       <array>
           <string>/Users/YOUR_USERNAME/NASA-APOD-Wallpaper/.venv/bin/python</string>
           <string>/Users/YOUR_USERNAME/NASA-APOD-Wallpaper/NasaWallpaper.py</string>
       </array>

       <!-- Run every day at 9:00 AM -->
       <key>StartCalendarInterval</key>
       <dict>
           <key>Hour</key>
           <integer>9</integer>
           <key>Minute</key>
           <integer>0</integer>
       </dict>

       <!-- Also run once when you log in -->
       <key>RunAtLoad</key>
       <true/>

       <key>StandardOutPath</key>
       <string>/tmp/apod-wallpaper.log</string>
       <key>StandardErrorPath</key>
       <string>/tmp/apod-wallpaper.log</string>
   </dict>
   </plist>
   ```

4. Turn it on:
   ```bash
   launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.apod.wallpaper.plist
   ```
5. Test it right away:
   ```bash
   launchctl kickstart gui/$(id -u)/com.apod.wallpaper
   ```
   The first scheduled run will ask for permission again, this time for **Python** to control *System Events*. Click **OK**.

If your Mac is asleep at the scheduled time, the job runs when it wakes up. If the Mac is completely shut down, that day's run is skipped, but `RunAtLoad` catches it the next time you log in.

To see what happened on the last run:
```bash
cat /tmp/apod-wallpaper.log
```

---

## Where Things Are Saved

| | Windows | macOS |
|---|---|---|
| Downloaded images | `C:\Users\<you>\Pictures\APOD\` | `/Users/<you>/Pictures/APOD/` |
| File name format | `apod-YYYY-MM-DD.jpg` | `apod-YYYY-MM-DD.jpg` |

Old images are **not** deleted automatically. Some high-resolution APOD images are large, so clear out the folder now and then if disk space matters.

---

## Troubleshooting

| Problem | Likely cause and fix |
|---|---|
| `ModuleNotFoundError: No module named 'requests'` | You ran the script with your system Python instead of the project's. Use `.venv\Scripts\python.exe` (Windows) or `.venv/bin/python` (macOS), and make sure Step 3 finished without errors. |
| `APOD is not an image, skipping today.` | Normal. Today's APOD is a video. Your wallpaper stays as it was. |
| `'python' is not recognized…` or the Microsoft Store opens | Python isn't on your PATH. Re-run the installer with **"Add python.exe to PATH"** checked, or use `py` instead of `python`. |
| `running scripts is disabled on this system` | You tried to activate the virtual environment. You don't need to. Use the `.venv\Scripts\python.exe …` commands exactly as shown. |
| macOS: `Setting Desktop Wallpaper Failed!` | The Automation permission was denied. Go to **System Settings → Privacy & Security → Automation** and allow Terminal (or Python) to control **System Events**. |
| macOS: scheduled run does nothing | Check `/tmp/apod-wallpaper.log`. "Operation not permitted" usually means the project is inside Documents, Desktop, or Downloads. Move it to your home folder and update the paths in the `.plist`. |
| Windows: scheduled task does nothing | In Task Scheduler, check the task's **Last Run Result** and **History** tab. Make sure **Start in** is filled in and the paths have no typos. |
| Windows: image looks stretched or cropped | Go to **Settings → Personalization → Background → Choose a fit** and pick **Fit** or **Fill**. Many APOD images are portrait-shaped. |
| `ConnectionError` or timeout | No internet, or a firewall or proxy is blocking `science.nasa.gov`. |
| `KeyError: 'hdurl'` | Occasionally a post doesn't include a high-resolution image link. The script stops for that day. Try again tomorrow. |

---

## Known Limitations

- **Windows and macOS only.** On Linux the script downloads the image but doesn't change the wallpaper.
- **macOS sets the main display only.** Additional monitors keep their current wallpaper.
- **Uses the newest post in NASA's feed.** That post can be a day behind the APOD website.
- **Files are always saved with a `.jpg` extension**, even on days NASA posts a PNG. Windows and macOS read the actual file contents, so the image still displays.
- **Some posts are marked as images but are really stills from a video.** On those days, the wallpaper may be a low-resolution thumbnail.

---

## Project Structure

```
NASA-APOD-Wallpaper/
├── NasaWallpaper.py   # The script
├── requirements.txt   # Python packages (same file for Windows and macOS)
├── .gitignore         # Keeps .venv and other clutter out of Git
├── LICENSE
└── README.md
```

---

## Uninstalling

1. **Remove the schedule:**
   - **Windows:** in Task Scheduler, right-click **NASA APOD Wallpaper** and choose **Delete**.
   - **macOS:**
     ```bash
     launchctl bootout gui/$(id -u)/com.apod.wallpaper
     rm ~/Library/LaunchAgents/com.apod.wallpaper.plist
     ```
2. Delete the `NASA-APOD-Wallpaper` folder.
3. (Optional) Delete `Pictures/APOD` to remove the downloaded images.

Your current wallpaper stays in place until you change it.

---

## Image Credits and Usage

APOD images belong to the photographers and institutions credited on each day's post. **Many are copyrighted and are not NASA public-domain images.** This tool downloads them for personal desktop use only. Check each image's credit before reusing it anywhere else. See [About APOD](https://science.nasa.gov/apod/about-apod/) for details.

---

## License

The **code** in this repository is released under the MIT License. See [LICENSE](LICENSE). The license does **not** cover the APOD images themselves; see [Image Credits and Usage](#image-credits-and-usage).

Thanks to NASA and the APOD editors for publishing the Astronomy Picture of the Day.
