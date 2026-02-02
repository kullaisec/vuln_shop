def audit_log(user):
    with open("/tmp/audit.log", "a") as f:
        f.write(user + "\n")