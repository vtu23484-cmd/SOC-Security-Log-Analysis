
import csv
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "sample_logs" / "auth.log"
REPORT_FILE = BASE_DIR / "reports" / "analysis_report.txt"
FAILED_LOGIN_THRESHOLD = 3


def analyze_logs():
    failed_by_ip = Counter()
    failed_by_user = Counter()
    successful_logins = 0
    failed_logins = 0
    invalid_records = 0
    total_records = 0

    with LOG_FILE.open("r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            if not row or all(not field.strip() for field in row):
                continue

            total_records += 1

            if len(row) != 4:
                invalid_records += 1
                continue

            timestamp, username, source_ip, status = [
                field.strip() for field in row
            ]

            if not timestamp or not username or not source_ip:
                invalid_records += 1
                continue

            if status not in {"FAILED", "SUCCESS"}:
                invalid_records += 1
                continue

            if status == "FAILED":
                failed_logins += 1
                failed_by_ip[source_ip] += 1
                failed_by_user[username] += 1
            else:
                successful_logins += 1

    lines = [
        "SOC SECURITY LOG ANALYSIS REPORT",
        "=" * 34,
        "Dataset: Synthetic training records",
        f"Total records processed: {total_records}",
        f"Successful logins: {successful_logins}",
        f"Failed logins: {failed_logins}",
        f"Invalid records: {invalid_records}",
        "",
        f"Source IPs with at least {FAILED_LOGIN_THRESHOLD} failed logins:",
    ]

    alerts_found = False

    for source_ip, count in sorted(failed_by_ip.items()):
        if count >= FAILED_LOGIN_THRESHOLD:
            lines.append(f"  {source_ip}: {count} failed attempts")
            alerts_found = True

    if not alerts_found:
        lines.append("  No IPs met the threshold.")

    lines.extend([
        "",
        f"User accounts with at least {FAILED_LOGIN_THRESHOLD} failed logins:",
    ])

    accounts_found = False

    for username, count in sorted(failed_by_user.items()):
        if count >= FAILED_LOGIN_THRESHOLD:
            lines.append(f"  {username}: {count} failed attempts")
            accounts_found = True

    if not accounts_found:
        lines.append("  No accounts met the threshold.")

    lines.extend([
        "",
        "Interpretation:",
        "Repeated failures warrant investigation but do not prove an attack.",
        "This report is based on synthetic data, not live security events.",
    ])

    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    REPORT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("\n".join(lines))
    print(f"\nReport saved to: {REPORT_FILE}")


if __name__ == "__main__":
    if not LOG_FILE.is_file():
        raise SystemExit(f"Log file not found: {LOG_FILE}")

    analyze_logs()
