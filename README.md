<p align="center">
  <h2 align="center">iLock</h2>
  <p align="center">Automatically lock your computer when your phone disconnect from the network!</p>
</p>

## Table of Contents

- [📥 Setup](#-setup)
- [✨ Run on Windows Startup](#-run-on-windows-startup)

## 📥 Setup

Create a `.env` file, put it in the root directory and fill the required fields.

| Field      | Description                    |
| ---------- | ------------------------------ |
| `TIMER`    | Seconds to wait between pings. |
| `PHONE_IP` | Your Phone IP on the network.  |

## ✨ Run on Windows Startup

1. Create a `iLock.bat` shortcut, then press `Ctrl+X` to Cut it.
2. Open the Run dialog with `WindowsKey+R` and enter `shell:startup`.
3. Press `Ctrl+V` while inside the opened folder to paste the shortcut.

Now you can see `iLock.bat` from the `Task Manager -> Startup` tab.

---

Made with Python and ❤️ 