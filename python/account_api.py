import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROCESS_SCRIPT = ROOT / "shell" / "process_account.sh"

def update_account(account_number: str, amount: float, transaction_type: str, priority: str = "NORMAL") -> dict:
    """Update account balance via mainframe service"""
    request = {
        "account_number": account_number,
        "amount": amount,
        "transaction_type": transaction_type,
        "currency": "USD",
        "channel": "NET",
        "user_id": "WEB001",
        "terminal_id": "WEB-TERM-001",
        "priority": priority
    }

    request_file = ROOT / "runtime_account_request.json"
    request_file.write_text(json.dumps(request), encoding="utf-8")

    result = subprocess.run(
        [str(PROCESS_SCRIPT), str(request_file)],
        capture_output=True,
        text=True,
        check=True,
    )

    return json.loads(result.stdout)

def get_account_balance(account_number: str) -> dict:
    """Get account balance via mainframe service"""
    request = {
        "account_number": account_number,
        "operation": "BALANCE_INQUIRY"
    }

    request_file = ROOT / "runtime_balance_request.json"
    request_file.write_text(json.dumps(request), encoding="utf-8")

    result = subprocess.run(
        [str(PROCESS_SCRIPT), str(request_file)],
        capture_output=True,
        text=True,
        check=True,
    )

    return json.loads(result.stdout)

if __name__ == "__main__":
    # Example usage
    print("Updating account A00000000001...")
    response = update_account("A00000000001", 5000.00, "DEP")
    print(f"Response: {response}")
    
    print("\nGetting account balance...")
    balance = get_account_balance("A00000000001")
    print(f"Balance: {balance}")
