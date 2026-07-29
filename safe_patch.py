import os, re

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith(('.html', '.js')):
            path = os.path.join(root, file)
            if '.git' in path or 'node_modules' in path: continue
            
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            original = content
            
            if file.endswith('.html'):
                content = re.sub(r'\bSOL\b', 'ETH', content)
                content = re.sub(r'\bsol\b', 'eth', content)
                content = re.sub(r'Solana', 'Robinhood Chain', content)
                content = re.sub(r'solana', 'robinhoodchain', content)
                content = re.sub(r'Pump\.fun', 'Pons Family', content)
                content = re.sub(r'pump\.fun', 'ponsfamily.com', content)
                content = re.sub(r'pumpfun', 'ponsfamily', content)
                content = re.sub(r'Pumpfun', 'Ponsfamily', content)
            elif file.endswith('.js'):
                content = content.replace('"SOL"', '"ETH"')
                content = content.replace('>SOL<', '>ETH<')
                content = content.replace('"Solana"', '"Robinhood Chain"')
                content = content.replace('>Solana<', '>Robinhood Chain<')
                content = content.replace('"Pump.fun"', '"Pons Family"')
                content = content.replace('>Pump.fun<', '>Pons Family<')
                content = content.replace('"pump.fun"', '"ponsfamily.com"')
                content = content.replace('>pump.fun<', '>ponsfamily.com<')
                
            if content != original:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f'Updated {path}')
