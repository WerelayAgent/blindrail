const fs = require('fs');
const path = require('path');

function fixMissingStrings(dir) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
            fixMissingStrings(fullPath);
        } else if (fullPath.endsWith('.js')) {
            let content = fs.readFileSync(fullPath, 'utf8');
            let original = content;
            
            // Fix the specific UI strings we found
            content = content.replace(/Connect a wallet on Solana to continue/g, 'Connect a wallet on Robinhood Chain to continue');
            content = content.replace(/ll need a wallet on Solana to continue/g, 'll need a wallet on Robinhood Chain to continue');
            content = content.replace(/sign in with your Solana account/g, 'sign in with your Robinhood Chain account');
            
            // Let's also find any other Capitalized 'Solana' that isn't part of an error name or URL or identifier
            // We can replace ' Solana ' with ' Robinhood Chain '
            content = content.replace(/ Solana /g, ' Robinhood Chain ');
            content = content.replace(/ Solana\b/g, ' Robinhood Chain');

            content = content.replace(/"Solana /g, '"Robinhood Chain ');
            content = content.replace(/>Solana /g, '>Robinhood Chain ');
            
            if (content !== original) {
                fs.writeFileSync(fullPath, content);
                console.log('Fixed', fullPath);
            }
        }
    }
}
fixMissingStrings('_next/static/chunks');
console.log('Done fixing JS chunks.');
