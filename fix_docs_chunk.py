import re

try:
    with open('_next/static/chunks/app/docs/page-0360294b17190271.js', 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    content = content.replace('DropRail', 'BlindRail')
    content = content.replace('droprail', 'blindrail')
    content = content.replace('"Drop"', '"Blind"')

    if content != original:
        with open('_next/static/chunks/app/docs/page-0360294b17190271.js', 'w', encoding='utf-8') as f:
            f.write(content)
        print('Fixed docs JS chunk')
except Exception as e:
    pass
