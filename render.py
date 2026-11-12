from banner import load_banner

def render_banner(text, banner_name="standard"):
    
    banner = load_banner(banner_name)
    
    text = text.replace("\\n", "\n")
    
    if text == "":
        return ""

    result = []

    parts = text.split("\n")
    
    for part in parts:
        if part == "":
            result.append("")
            continue
            
        for row in range(8):
            line_output = ""
            for char in part:
                if char in banner:
                    line_output += banner[char][row]
                else:
                
                    line_output += banner.get(" ", [""] * 8)[row]
            result.append(line_output)
            
    return "\n".join(result)