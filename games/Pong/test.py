def detect_invisible_chars(text):
    suspicious = []
    for i, char in enumerate(text):
        if char.isspace() and ord(char) != 32:  # 32 is regular space (U+0020)
            suspicious.append((i, hex(ord(char)), char.encode('unicode-escape').decode()))
    return suspicious

# Example usage
code_sample = "print('Hello')\u00A0  # <-- NBSP here"
issues = detect_invisible_chars(code_sample)
if issues:
    print("Suspicious characters found:")
    for pos, hex_val, esc in issues:
        print(f"Position {pos}: {hex_val} ({esc})")
else:
    print("No suspicious spaces detected.")
