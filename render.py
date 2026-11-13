from banner import load_banner

def render_art(text, banner_name="standard"):
    # Load the character dictionary for the requested banner style
    banner = load_banner(banner_name)
    
    # Handle literal backslash-n typed in the terminal
    text = text.replace("\\n", "\n")
    
    if text == "":
        return ""
        
    # Split input text by newlines so multi-line inputs stack correctly
    lines = text.split("\n")
    
    output_rows = []
    
    for line in lines:
        # If a line is empty, just append an empty row
        if line == "":
            output_rows.append("")
            continue
        
        # Each ASCII character is exactly 8 lines tall (rows 0 to 7)
        for row_idx in range(8):
            current_row_str = ""
            for char in line:
                if char in banner:
                    current_row_str += banner[char][row_idx]
                else:
                    # Fallback to a space if a character is missing
                    current_row_str += banner[" "][row_idx]
            output_rows.append(current_row_str)
                    
    return "\n".join(output_rows)