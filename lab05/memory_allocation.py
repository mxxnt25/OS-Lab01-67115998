import os
import time

import psutil


def print_memory_usage():
    """Show the physical memory currently used by this process."""
    process = psutil.Process(os.getpid())
    mem_mb = process.memory_info().rss / (1024 * 1024)
    print(f"[OS Monitor] Current Physical RAM Usage: {mem_mb:.2f} MB")


def main():
    print(f"--- AI Model Memory Allocation (PID: {os.getpid()}) ---")
    print_memory_usage()

    print("\nLoading a large Neural Network layer into memory...")
    time.sleep(2)

    # Create a Python list with 10 million entries.
    ai_model_weights = [0.0] * 10_000_000

    print("Model loaded successfully!")
    print_memory_usage()

    print("\nProgram is sleeping. Open another terminal and run 'htop'.")
    time.sleep(30)


if __name__ == "__main__":
    main()