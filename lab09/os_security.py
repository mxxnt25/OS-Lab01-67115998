# os_security.py

import os
import stat


def main():
    secure_file = "secret_config.json"

    # Clean up the demonstration file from a previous run
    if os.path.exists(secure_file):
        os.chmod(secure_file, 0o666)
        os.remove(secure_file)

    # Create a demonstration file
    with open(secure_file, "w") as f:
        f.write('{"api_key": "12345XYZ"}')

    print(f"Created {secure_file}.")

    # Owner can read; group and others have no access
    print("Locking file permissions to Read-Only (0o400)...")
    os.chmod(secure_file, 0o400)

    permissions = stat.filemode(os.stat(secure_file).st_mode)
    print(f"New Permissions: {permissions}")

    # Try to append data
    print("\nAttempting to overwrite the file...")

    try:
        with open(secure_file, "a") as f:
            f.write("\nMALICIOUS HACKER DATA")

        print("Success! Data written.")

    except PermissionError as e:
        print(f">>> [OS KERNEL BLOCKED] PermissionError: {e}")
        print(">>> The Operating System successfully protected the file!")


if __name__ == "__main__":
    main()