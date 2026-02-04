
import os

SITE_DIR = r"c:\dev\docs\site"
OLD_URL = "https://docs.astral.sh"
NEW_URL = "http://localhost:8000"

def fix_links():
    count = 0
    for root, dirs, files in os.walk(SITE_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Read as binary to avoid encoding issues with images etc, 
                # but valid text files will process fine if we decode/encode safely 
                # or just treat as binary for replace if simple ascii.
                # However, encoding might be variable. 
                # Let's try text mode with utf-8, ignoring errors? 
                # It's a static site, mostly html/js/css which should be utf-8.
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                
                if OLD_URL in content:
                    new_content = content.replace(OLD_URL, NEW_URL)
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Fixed: {file_path}")
                    count += 1
            except Exception as e:
                print(f"Skipping {file_path}: {e}")
    
    print(f"Total files fixed: {count}")

if __name__ == "__main__":
    fix_links()
