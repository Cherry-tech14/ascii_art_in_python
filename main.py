import sys
from render import render_banner

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <string> [banner]")
        return

    text = sys.argv[1]
    
    # Check if a banner style was provided as the second argument, default to 'standard'
    banner_name = "standard"
    if len(sys.argv) >= 3:
        banner_name = sys.argv[2]

    # Render and print the ASCII art using the requested banner
    result = render_banner(text, banner_name)
    print(result)

if __name__ == "__main__":
    main()