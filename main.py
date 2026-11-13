import sys
from render import render_art

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <string> [banner]")
        return
        
    text = sys.argv[1]
    banner_name = "standard"
    

    if len(sys.argv) >= 3:
        banner_name = sys.argv[2]
        
    try:
        result = render_art(text, banner_name)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()