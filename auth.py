from pathlib import Path
from ytmusicapi import YTMusic, setup as ytm_setup

CONFIG_DIR = Path.home() / ".uniplay"
AUTH_FILE  = CONFIG_DIR / "headers.json"


def setup_auth():
    CONFIG_DIR.mkdir(exist_ok=True)
    print("=== UniPlay Setup — YouTube Music Auth ===\n")
    print("1. Open https://music.youtube.com in your browser and log in.")
    print("2. Press F12 to open DevTools.")
    print("3. Go to the Console tab and run:")
    print()
    print("     copy(document.cookie)")
    print()
    print("4. Paste the cookie string below and press Enter:\n")

    cookie = input("> ").strip()

    if not cookie or "SAPISID" not in cookie:
        print("\nWarning: Cookie doesn't look right (missing SAPISID). Auth may fail.")

    headers_raw = (
        f"cookie: {cookie}\n"
        "x-goog-authuser: 0\n"
        "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36\n"
    )

    ytm_setup(filepath=str(AUTH_FILE), headers_raw=headers_raw)

    import json
    data = json.loads(AUTH_FILE.read_text())
    if "authorization" not in {k.lower() for k in data}:
        data["authorization"] = "SAPISIDHASH"
        AUTH_FILE.write_text(json.dumps(data, indent=4))

    print(f"\nAuth saved to {AUTH_FILE}")
    print("Run 'python main.py' to launch UniPlay.")


def get_ytmusic() -> YTMusic:
    if not AUTH_FILE.exists():
        raise FileNotFoundError(
            f"No auth file found at {AUTH_FILE}.\n"
            "Run 'python main.py setup' first."
        )
    return YTMusic(auth=str(AUTH_FILE))


def ytmusic_or_none() -> YTMusic | None:
    try:
        return get_ytmusic()
    except Exception:
        return None
