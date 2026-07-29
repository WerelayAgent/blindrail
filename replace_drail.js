const fs = require('fs');
const path = require('path');

function replaceDrail(dir) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
            if (file !== '.git' && file !== 'node_modules' && file !== '.next') {
                replaceDrail(fullPath);
            }
        } else if (fullPath.endsWith('.js') || fullPath.endsWith('.html')) {
            let content = fs.readFileSync(fullPath, 'utf8');
            let original = content;
            
            // Replace $BRAIL to $BRAIL
            content = content.replace(/\$BRAIL/g, '$BRAIL');
            // Replace BRAIL to BRAIL
            content = content.replace(/\bDRAIL\b/g, 'BRAIL');
            // Check for lowercase brail just in case
            content = content.replace(/\bdrail\b/g, 'brail');
            
            if (content !== original) {
                fs.writeFileSync(fullPath, content);
                console.log('Fixed', fullPath);
            }
        }
    }
}
replaceDrail('.');
console.log('Done replacing BRAIL with BRAIL.');
