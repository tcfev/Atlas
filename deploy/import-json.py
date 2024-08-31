import json
import os
import datetime

# Step 1: Read the JSON file
json_file_path = 'static/data/data.json'
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Step 2: Define the output directory
output_dir = 'src/content/org-pages/'
os.makedirs(output_dir, exist_ok=True)

# Step 3: Process each entry in the JSON data
for entry in data:
    # Step 4: Determine the title
    title = entry.get('id')
    
    # Step 5: Create the Markdown content
    markdown_content = f"""---
title: "{title}"
date: "2024-08-22"
updated: "{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"
headerBg: "background-image: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);"
---

**Organization Type**: {entry.get('org_type', 'N/A')}  
**Logo**: ![Logo]({entry.get('logo', 'N/A')})  
**Locations**: {entry.get('locations', 'N/A')}  
**Internet Address**: [Website]({entry.get('internet_address', 'N/A')})  
**Email**: {entry.get('email', 'N/A')}  
**Phone**: {entry.get('phone', 'N/A')}  
**Expertise**: {entry.get('expertise', 'N/A')}  
"""

    # Step 6: Write to a file
    output_file_path = os.path.join(output_dir, f"{title}.md")
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(markdown_content)