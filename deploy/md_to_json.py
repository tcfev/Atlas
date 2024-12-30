import os
import json
import re
import argparse

def extract_frontmatter(content):
    """Extract frontmatter from markdown content"""
    pattern = r'^---\n(.*?)\n---'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        frontmatter = {}
        for line in match.group(1).split('\n'):
            if ':' in line:
                # Split only on first colon
                key, value = line.split(':', 1)
                # Remove quotes and whitespace
                value = value.strip().strip('"\'')
                frontmatter[key.strip()] = value
        return frontmatter
    return None

def process_directory(directory_path, output_file):
    """Process all markdown files in directory and create JSON"""
    entries = []
    
    # Walk through all files in directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.md'):
            file_path = os.path.join(directory_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    frontmatter = extract_frontmatter(content)
                    if frontmatter:
                        entries.append(frontmatter)
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

    # Write to JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(entries, f, ensure_ascii=False, indent=4)
    
    print(f"Successfully processed {len(entries)} files into {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Convert markdown frontmatter to JSON')
    parser.add_argument('directory', help='Directory containing markdown files')
    parser.add_argument('--output', '-o', default='output.json', help='Output JSON file path')
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.directory):
        print(f"Error: {args.directory} is not a valid directory")
        return
    
    process_directory(args.directory, args.output)

if __name__ == "__main__":
    main()
