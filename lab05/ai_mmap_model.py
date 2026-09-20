import mmap
import os

import psutil


def print_memory():
    """Show the physical memory currently used by this process."""
    process = psutil.Process(os.getpid())
    mem_mb = process.memory_info().rss / (1024 * 1024)
    print(f"[OS Monitor] Physical RAM Usage: {mem_mb:.2f} MB")


def main():
    file_path = "fake_llm_weights.bin"

    # 1. Create a 50 MB file containing zero bytes.
    print("Creating a 50MB fake LLM file on disk...")
    with open(file_path, "wb") as f:
        f.write(b"\x00" * (50 * 1024 * 1024))

    print("\nBefore mapping:")
    print_memory()

    # 2. Map the file into the process's virtual address space.
    print("\nMapping the 50MB file into virtual memory...")
    with open(file_path, "r+b") as f:
        with mmap.mmap(f.fileno(), 0) as mm:
            print("\nAfter mapping:")
            print_memory()

            # 3. Read one byte from the mapped file.
            print("\nAccessing weight at index 25,000,000...")
            weight = mm[25_000_000]
            print(f"Weight value accessed successfully: {weight}")

    # 4. Delete the temporary file after closing it.
    os.remove(file_path)
    print("\nTemporary model file removed.")


if __name__ == "__main__":
    main()