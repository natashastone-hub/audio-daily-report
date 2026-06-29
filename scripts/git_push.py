import subprocess, os, sys

token = sys.argv[1]
repo_path = sys.argv[2] if len(sys.argv) > 2 else r'C:\Users\Administrator\.openclaw\workspace\audio-daily-report'
branch = sys.argv[3] if len(sys.argv) > 3 else 'main'

os.chdir(repo_path)
remote_url = f'https://oauth2:{token}@github.com/natashastone-hub/audio-daily-report.git'
remote_url = f'https://{token}@github.com/natashastone-hub/audio-daily-report.git'

subprocess.run(['git', 'remote', 'set-url', 'origin', remote_url], check=True)
result = subprocess.run(['git', 'push', 'origin', branch], capture_output=True, text=True)
print(result.stdout)
if result.stderr:
    print(result.stderr)
