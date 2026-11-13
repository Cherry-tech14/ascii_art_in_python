import os

def load_banner(banner_name):
    filename = banner_name + ".txt"
    
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Could not find banner file: '{filename}'")
    
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    lines = content.splitlines()
    
    characters = {}

    for i in range(32, 127):
        
        start_line = 1 + (i - 32) * 9
        char_lines = lines[start_line : start_line + 8]
        characters[chr(i)] = char_lines
        
    return characters