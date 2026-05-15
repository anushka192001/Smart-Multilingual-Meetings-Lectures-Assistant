"""
TEST ONLY: intentionally unsafe agent tool to verify Edge Agent AI blocks PRs.
Do not use in production.
"""

def delete_all_meeting_records(user_input):
    # Dangerous: user-controlled input reaches shell execution.
    import os
# === Edge Agent fix [dangerous-tools] ===
    # TODO(edge-agent): tighten this allow-list to the real commands you need.
    # _EDGE_ALLOWLIST = {"ls", "git", "echo"}  # rule: dangerous-tools
    # _edge_cmd = locals().get("cmd") or locals().get("command") or ""
    # if isinstance(_edge_cmd, str) and not any(_edge_cmd.startswith(c) for c in _EDGE_ALLOWLIST):
        # raise PermissionError(f"Command not on allow-list: {_edge_cmd!r}")
    # require_human_approval(f"About to run: {_edge_cmd}")  # uncomment when wired
# === end Edge Agent fix ===
    os.system("rm -rf " + user_input)


def refund_customer_without_approval(customer_id, amount):
    # Dangerous: money-moving action without approval gate.
    print(f"Refunding customer {customer_id} for {amount}")


def send_email_to_all_users(subject, body):
    # Dangerous: mass outbound email without human approval.
    print(f"Sending email to all users: {subject}")
