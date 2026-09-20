# Page size used by this simulator.
PAGE_SIZE = 1000

# Map each logical page to a physical frame.
os_page_table = {
    0: 12,
    1: 45,
    2: 8,
    3: 102,
    4: 15,
    5: 33,
}


def translate_address(logical_address):
    """Simulate address translation using a page table."""
    print(f"\n[MMU] Requesting Logical Address: {logical_address}")

    # 1. Split the logical address into a page number and an offset.
    page_number = logical_address // PAGE_SIZE
    offset = logical_address % PAGE_SIZE

    print(f"        -> Computed Page Number: {page_number}")
    print(f"        -> Computed Offset: {offset}")

    # 2. Look up the physical frame.
    if page_number not in os_page_table:
        print("        -> [OS ERROR] Page is not mapped in this simulator.")
        return None

    frame_number = os_page_table[page_number]
    print(f"        -> Page Table Lookup: Found in Frame {frame_number}")

    # 3. Calculate the physical address.
    physical_address = (frame_number * PAGE_SIZE) + offset
    print(
        f"        -> [SUCCESS] Translated Physical Address: "
        f"{physical_address}"
    )

    return physical_address


def main():
    print("--- AI Model Address Translation Simulator ---")

    # Scenario A
    translate_address(250)

    # Scenario B
    translate_address(3450)

    # Scenario C: This page is not in the simulated page table.
    translate_address(9999)


if __name__ == "__main__":
    main()