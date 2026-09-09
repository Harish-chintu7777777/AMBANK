import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "shell" / "health_check.sh"

def check_mainframe() -> int:
    """Check mainframe service health"""
    completed = subprocess.run([str(SCRIPT)], check=False)
    return completed.returncode

if __name__ == "__main__":
    raise SystemExit(check_mainframe())
