def monitor_server(duration_minutes):
    print(f"--- Starting Server Monitor for {duration_minutes} Minutes ---")

    for minute in range(1, duration_minutes + 1):
        # Rule 1: Every 30 minutes (The most critical/rare task)
        if minute % 30 == 0:
            print(f"Minute {minute}: [CRITICAL] Performing Full Database Backup...")

        # Rule 2: Every 10 minutes
        elif minute % 10 == 0:
            print(f"Minute {minute}: [SECURITY] Running automated security scan...")

        # Rule 3: Every 2 minutes
        elif minute % 2 == 0:
            print(f"Minute {minute}: [HEALTH] Heartbeat signal sent.")

        # Standard minute
        else:
            # We don't want to spam the logs, so we just pass
            pass


# Run the monitor for 1 hour
monitor_server(60)
