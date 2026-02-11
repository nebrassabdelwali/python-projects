def analyze_log(file_path):
    suspicious_ips = {}
    
    try:
        with open(file_path, "r") as file:
            for line in file:
                if "Failed login" in line:
                    parts = line.split()
                    ip = parts[-1]
                    
                    if ip in suspicious_ips:
                        suspicious_ips[ip] += 1
                    else:
                        suspicious_ips[ip] = 1

        print("\n--- Suspicious Activity Report ---")
        for ip, attempts in suspicious_ips.items():
            if attempts >= 3:
                print(f"⚠️ ALERT: {ip} has {attempts} failed login attempts")

    except FileNotFoundError:
        print("Log file not found.")


if __name__ == "__main__":
    file_path = input("Enter log file path: ")
    analyze_log(file_path)
