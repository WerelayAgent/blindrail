import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # Text replacements preserving case where possible
    content = re.sub(r'DropRail', 'BlindRail', content)
    content = re.sub(r'droprail', 'blindrail', content)
    content = re.sub(r'DROPRAIL', 'BLINDRAIL', content)
    
    # Domain & Twitter replacements
    content = re.sub(r'blindrail\.dev', 'blindrail.com', content, flags=re.IGNORECASE)
    content = re.sub(r'x\.com/BlindRail', 'x.com/blindrail', content, flags=re.IGNORECASE)
    
    # Wallet address -> coming soon on pump.fun
    content = content.replace('DweWj1v5boinFHehjNAbxhyhMdLxwMmmcyZaYrBwpump', 'coming soon on pump.fun')
    
    # Patch links for static hosting (prevent 404s when JS router tries to load /dashboard)
    if filepath.endswith('.html'):
        content = content.replace('href="/dashboard"', 'href="/dashboard.html"')
        content = content.replace('href="/use-cases"', 'href="/use-cases.html"')
        content = content.replace('href="/stake"', 'href="/stake.html"')
        content = content.replace('href="/docs"', 'href="/docs.html"')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")

def main():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(('.html', '.js', '.css', '.json', '.webmanifest')):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
