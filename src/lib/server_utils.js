import { readdirSync } from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export function getAllOPPaths() {
    const postsDirectory = path.join(__dirname, '..', 'content', 'org-pages');
    try {
        const files = readdirSync(postsDirectory);
        const opPaths = files
            .filter(file => file.endsWith('.md'))
            .map(file => `/op/${file.replace('.md', '')}`);
        return opPaths;
    } catch (err) {
        console.error('Error reading directory:', err);
        throw err;
    }
}