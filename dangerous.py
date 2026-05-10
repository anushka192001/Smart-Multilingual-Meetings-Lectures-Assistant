"""
TEST ONLY: intentionally unsafe agent tool to verify Edge Agent AI blocks PRs.
Do not use in production.
"""

def delete_all_meeting_records(user_input):
    # Dangerous: user-controlled input reaches shell execution.
    import os
    os.system("rm -rf " + user_input)


def refund_customer_without_approval(customer_id, amount):
    # Dangerous: money-moving action without approval gate.
    print(f"Refunding customer {customer_id} for {amount}")


def send_email_to_all_users(subject, body):
    # Dangerous: mass outbound email without human approval.
    print(f"Sending email to all users: {subject}")
