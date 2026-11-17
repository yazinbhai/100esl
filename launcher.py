"""
Kerala Talking Statue & Toy Kiosk - Windows Application Launcher
================================================================
This script:
1. Prevents Windows PC from sleeping / turning off display (SetThreadExecutionState).
2. Serves the interactive kiosk web app locally on http://localhost:8585.
3. Launches Microsoft Edge in native standalone Desktop App Mode (--app=http://localhost:8585)
   with automatic microphone permission authorization for unattended statue operation.
4. Keeps the kiosk running 24/7 for Kerala school students.
"""

import sys
import os
import time
import ctypes
import threading
import subprocess
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PORT = 8585
WEB_DIR = os.path.dirname(os.path.abspath(__file__))
if os.path.exists(os.path.join(WEB_DIR, "web", "index.html")):
    WEB_DIR = os.path.join(WEB_DIR, "web")

# Windows Power Management Flags
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

def set_keep_awake():
    """Instruct Windows kernel to prevent system sleep and display timeout."""
    try:
        res = ctypes.windll.kernel32.SetThreadExecutionState(
            ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
        )
        if res:
            print("[+] Windows Power Management: System & Display Sleep PREVENTED (Always Awake Active)")
        else:
            print("[!] Warning: SetThreadExecutionState returned 0")
    except Exception as e:
        print(f"[!] Could not set execution state: {e}")

def restore_sleep():
    """Restore normal Windows power behavior on shutdown."""
    try:
        ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
        print("[+] Windows Power Management restored to standard settings.")
    except Exception:
        pass

class KioskHTTPHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def log_message(self, format, *args):
        # Keep console output clean
        return

def run_server():
    server_address = ('127.0.0.1', PORT)
    httpd = ThreadingHTTPServer(server_address, KioskHTTPHandler)
    print(f"[+] Kiosk Web Server running at http://127.0.0.1:{PORT}")
    httpd.serve_forever()

def find_edge_path():
    possible_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\Application\msedge.exe"),
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    ]
    for p in possible_paths:
        if os.path.exists(p):
            return p
    return None

def launch_kiosk_window():
    edge_exe = find_edge_path()
    target_url = f"http://127.0.0.1:{PORT}/index.html"

    if edge_exe:
        print(f"[+] Launching Windows App window using: {edge_exe}")
        # Launch in standalone App mode (no URL bar, no tabs) with auto-granted microphone permission
        cmd = [
            edge_exe,
            f"--app={target_url}",
            "--start-maximized",
            "--use-fake-ui-for-media-stream",  # Auto-allows mic without prompting every time
            "--autoplay-policy=no-user-gesture-required",
            "--disable-features=Translate"
        ]
        return subprocess.Popen(cmd)
    else:
        print("[!] Native browser executable not found. Opening in default browser...")
        import webbrowser
        webbrowser.open(target_url)
        return None

def main():
    print("=" * 65)
    print("      KERALA TALKING STATUE & TOY KIOSK (100 ENGLISH Q&A)     ")
    print("=" * 65)

    # 1. Prevent PC from sleeping
    set_keep_awake()

    # 2. Start Local HTTP Server
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    time.sleep(1)

    # 3. Launch App Window
    process = launch_kiosk_window()

    print("\n[✓] Statue Kiosk is now active!")
    print("    - Microphone & Speaker are ready.")
    print("    - Students can ask any of the 100 questions.")
    print("    - Press Ctrl+C in this console to exit.\n")

    try:
        if process:
            # Keep awake while process is running
            while process.poll() is None:
                # Refresh keep-awake heartbeat every 60 seconds
                time.sleep(60)
                set_keep_awake()
        else:
            while True:
                time.sleep(60)
                set_keep_awake()
    except KeyboardInterrupt:
        print("\n[*] Shutting down Talking Statue Kiosk...")
    finally:
        restore_sleep()

if __name__ == "__main__":
    main()
