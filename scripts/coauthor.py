#!/usr/bin/env python3

import json
import os
import sys
import urllib.error
import urllib.request

API = "https://api.github.com/users/{}"

def fetch_user(username: str) -> dict:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "coauthor-line-script",
    }
    token = os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    req = urllib.request.Request(API.format(username), headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        msg = e.read().decode("utf-8", "replace")
        print(f"error: GitHub API returned {e.code} {e.reason} for '{username}'", file=sys.stderr)
        if msg.strip():
            print(msg, file=sys.stderr)
        raise SystemExit(2)

def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[1] in ("-h", "--help"):
        print(f"Usage: {argv[0]} <github-username>", file=sys.stderr)
        return 1

    username = argv[1].strip()
    data = fetch_user(username)

    login = data.get("login") or username
    uid = data.get("id")
    display_name = data.get("name") or login

    if uid is None:
        print("error: missing 'id' in API response", file=sys.stderr)
        return 2

    noreply_email = f"{uid}+{login}@users.noreply.github.com"
    print(f"Co-authored-by: {display_name} <{noreply_email}>")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

