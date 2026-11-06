
import subprocess

def run_command(command, title, timeout):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout
        )

        print(result.stdout)

        if result.stderr:
            print("Additional information:")
            print(result.stderr)

    except FileNotFoundError:
        print("Command not found. Check that Windows network tools are available.")

    except subprocess.TimeoutExpired:
        print("The command took too long and was stopped.")

def main():
    destination = input("Enter destination (press Enter for google.com): ").strip()

    if not destination:
        destination = "google.com"

    print("\nNetwork Diagnostics for:", destination)

    # Test network connectivity and response time
    run_command(
        ["ping", "-n", "4", destination],
        "PING TEST",
        20
    )

    # Display the route taken by packets
    run_command(
        ["tracert", "-d", "-h", "10", "-w", "1000", destination],
        "TRACEROUTE TEST",
        60
    )

if __name__ == "__main__":
    main()
