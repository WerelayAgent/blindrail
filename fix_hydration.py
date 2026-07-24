import os
import re

updated = False
for root, _, files in os.walk('_next/static/chunks'):
    for file in files:
        if file.endswith('.js'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            original = content
            
            # Replace exactly "Drop" with "Blind"
            content = content.replace('"Drop"', '"Blind"')
            
            if content != original:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f'Fixed {path}')
                updated = True

if updated:
    os.system('git add -A ; git commit -m "fix: nextjs hydration restoring DropRail" ; git push')
else:
    print('Nothing to update')
