import os
import sys
import base64
import json
import urllib.request
import urllib.error

REPO_OWNER = "smahammadarshad08-debu"
REPO_NAME = "conclaveindia"
BRANCH = "main"

print("=" * 65)
print(" AccessMap — Direct Python GitHub Uploader (No Git Required)")
print(f" Target: https://github.com/{REPO_OWNER}/{REPO_NAME}")
print("=" * 65)

# Prompt for GitHub Personal Access Token if not in environment
token = os.environ.get("GITHUB_TOKEN", "").strip()
if not token:
    print("\nTo push files without installing Git, a GitHub Personal Access Token is needed.")
    print("Generate one in 30 seconds at: https://github.com/settings/tokens (classic token with 'repo' scope)")
    print()
    token = input("Enter your GitHub Personal Access Token: ").strip()

if not token:
    print("\n[!] No token provided. Exiting.")
    sys.exit(1)

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "AccessMap-Uploader"
}

# Verify access to repository
repo_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"
req = urllib.request.Request(repo_url, headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        repo_data = json.loads(resp.read().decode())
        print(f"[OK] Connected to repository: {repo_data['full_name']} (Default branch: {repo_data.get('default_branch', 'main')})")
        BRANCH = repo_data.get('default_branch', 'main')
except urllib.error.HTTPError as e:
    if e.code == 404:
        print(f"\n[!] Repository not found or token lacks access: {repo_url}")
        print("Please verify the repository exists and your token has 'repo' permission.")
    elif e.code == 401:
        print("\n[!] Unauthorized: Invalid GitHub token. Please verify your token.")
    else:
        print(f"\n[!] GitHub API Error: {e.code} - {e.reason}")
    sys.exit(1)
except Exception as e:
    print(f"\n[!] Connection error: {e}")
    sys.exit(1)

# Files to upload
base_dir = os.path.dirname(os.path.abspath(__file__))
ignored_dirs = {'.git', '__pycache__', '.venv', 'node_modules', 'scratch'}
ignored_files = {'github_uploader.py', '.DS_Store', 'Thumbs.db'}

files_to_upload = []
for root, dirs, files in os.walk(base_dir):
    dirs[:] = [d for d in dirs if d not in ignored_dirs]
    for file in files:
        if file in ignored_files or file.endswith('.pyc') or file.endswith('.log'):
            continue
        rel_path = os.path.relpath(os.path.join(root, file), base_dir).replace('\\', '/')
        files_to_upload.append((os.path.join(root, file), rel_path))

print(f"\nFound {len(files_to_upload)} files to upload to {BRANCH} branch:\n")

for local_path, remote_path in files_to_upload:
    print(f"Uploading: {remote_path} ...", end=" ", flush=True)

    with open(local_path, "rb") as f:
        content_bytes = f.read()

    b64_content = base64.b64encode(content_bytes).decode("ascii")

    # Check if file exists to get its SHA (required for updating)
    file_api_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{remote_path}?ref={BRANCH}"
    sha = None
    try:
        check_req = urllib.request.Request(file_api_url, headers=headers)
        with urllib.request.urlopen(check_req) as resp:
            data = json.loads(resp.read().decode())
            sha = data.get("sha")
    except urllib.error.HTTPError as e:
        if e.code != 404:
            print(f"[!] Warning checking {remote_path}: {e.code}")

    # Prepare payload
    payload = {
        "message": f"feat: upload {remote_path} for AccessMap platform",
        "content": b64_content,
        "branch": BRANCH
    }
    if sha:
        payload["sha"] = sha

    put_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{remote_path}"
    put_req = urllib.request.Request(
        put_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={**headers, "Content-Type": "application/json"},
        method="PUT"
    )

    try:
        with urllib.request.urlopen(put_req) as resp:
            print("[SUCCESS]")
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode()
        print(f"[FAILED: {e.code}] {err_msg}")

print("\n" + "=" * 65)
print(f" All done! Visit your repository at:")
print(f" https://github.com/{REPO_OWNER}/{REPO_NAME}")
print("=" * 65)
input("\nPress Enter to exit...")
