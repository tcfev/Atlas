import json
import os
import datetime
import re
json_file_path = 'static/data/data.json'
output_dir = 'src/content/org-pages/'


def log(message):
    print(f'{datetime.datetime.now()} - {message}')

def _(t):
    # remove \n and \r from the string, and strip the trailing spaces
    return str(t).replace('\n', '').replace('\r', '').strip()

def getMarkdownContent(
    entry: dict,
    title: str
):

    return \
        f"""---
title: "{_(title)}"
id: "{_(entry.get('id', ''))}"
org_type: "{_(entry.get('org_type', ''))}"
pageLink: "{_(entry.get('pageLink', ''))}"
logo: "{_(entry.get('logo', ''))}"
name_fa: "{_(entry.get('name_fa', ''))}"
name_en: "{_(entry.get('name_en', ''))}"
name_short: "{_(entry.get('name_short', ''))}"
locations: "{_(entry.get('locations', ''))}"
post_location: "{_(entry.get('post_location', ''))}"
internet_address: "{_(entry.get('internet_address', ''))}"
email: "{_(entry.get('email', ''))}"
phone: "{_(entry.get('phone', ''))}"
about: "{_(entry.get('about', ''))}"
expertise: "{_(entry.get('expertise', ''))}"
history: "{_(entry.get('history', ''))}"
manifesto: "{_(entry.get('manifesto', ''))}"
coc: "{_(entry.get('coc', ''))}"
estimation_of_members: "{_(entry.get('estimation_of_members', ''))}"
political_orientation: "{_(entry.get('political_orientation', ''))}"
mark_for_edit: "{_(entry.get('mark_for_edit', ''))}"
social_telegram: "{_(entry.get('social_telegram', ''))}"
social_facebook: "{_(entry.get('social_facebook', ''))}"
social_youtube: "{_(entry.get('social_youtube', ''))}"
social_x: "{_(entry.get('social_x', ''))}"
social_instagram: "{_(entry.get('social_instagram', ''))}"
created_at: "{_(entry.get('created_at', ''))}"
updated_at: "{_(entry.get('updated_at', ''))}"
mark_for_delete: "{_(entry.get('mark_for_delete', ''))}"
delete_reason: "{_(entry.get('delete_reason', ''))}"
deleted_at: "{_(entry.get('deleted_at', ''))}"
headerBg: "background-image: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);"
---
"""

def addPageLink(entry: dict, title: str):
    entry["pageLink"] = f"/op/{title}"
    return entry

def getTitle(entry: dict):
    title = entry.get('name_fa')
    if title == "":
        title = entry.get('name_en')
    if title == "":
        title = str(entry.get('name_short'))
    if title == "":
        title = str(entry.get('id'))
    # repl ace empty spaces ine the name with -
    title = title.replace(' ', '-')

    return title


def delete_all_pages():
    for filename in os.listdir(output_dir):
        file_path = os.path.join(output_dir, filename)
        os.remove(file_path)
        log("File deleted: " + file_path)


def mapIDtoFileName(output_dir):
    mapped = {}
    for filename in os.listdir(output_dir):
        file_path = os.path.join(output_dir, filename)

        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()

        delimiter_positions = [m.start()
                               for m in re.finditer(r'^---$', content, re.MULTILINE)]

        # Step 2: Check if there are at least two delimiters
        if len(delimiter_positions) >= 2:
            # Step 3: Extract the section between the first two delimiters
            section_content = content[delimiter_positions[0]:delimiter_positions[1]]

            # Step 4: Search for the ID within the extracted section
            id_pattern = re.compile(r'id:\s*"(.*?)"')
            match = id_pattern.search(section_content)

            # Step 5: Check if ID is found
            if match:
                id_from_file = match.group(1)
                mapped[id_from_file] = filename
            else:
                print(file_path)
                log("No ID found in delimited section of file, the file will be deleted: " + file_path)
                os.remove(file_path)
        else:
            print(file_path)
            log("No delimited section found in file, the file will be deleted: " + file_path)
            os.remove(file_path)
    return mapped


def update_file_content(file_path, entry, title):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        split_by = content.split('---')
        if len(split_by) < 2:
            log(f"File {file_path} is not in the correct format")
            return
        file_header = split_by[1]
        correct_header = getMarkdownContent(
            entry, title=getTitle(entry)).split('---')[1]
        if file_header != correct_header:
            print(file_header)
            print(correct_header)
            log(f"Header mismatch in file: {file_path}")
            # Update file content
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(getMarkdownContent(entry, title))
                log(f"File updated: {file_path}")
    except Exception as e:
        log(f"Error updating file {file_path}: {e}")


def create_new_file(file_path, entry, title):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(getMarkdownContent(entry, title))
            log(f'File created: {file_path}')
    except Exception as e:
        log(f"Error creating file {file_path}: {e}")


def process_entry(entry, output_dir, mapped_file):
    title = getTitle(entry)
    filename = title + '.md'
    file_path = os.path.join(output_dir, filename)
    # Check if entry ID is in mapped_file
    entry_id = str(entry.get('id'))
    if entry_id in mapped_file:
        filename = mapped_file[entry_id]
        file_path = os.path.join(output_dir, filename)
        correct_title = f"{getTitle(entry)}.md"
        if filename != correct_title:
            log(f"{filename} != {correct_title}")
            # Rename file to correct_title.md
            new_file_path = os.path.join(output_dir, correct_title)
            os.rename(file_path, new_file_path)
            file_path = new_file_path
            # Update mapped_file
            mapped_file[entry_id] = correct_title
            log(f"File renamed: {file_path} -> {new_file_path}")
        # Check and update file content if necessary
        update_file_content(file_path, entry, title)
    else:
        create_new_file(file_path, entry, title)


def main():
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # replace ever \n and \r with empty string, remove trailing spaces
    for entry in data:
        for key, value in entry.items():
            entry[key] = _(value)

    os.makedirs(output_dir, exist_ok=True)

    mapped_file = mapIDtoFileName(output_dir)

    for entry in data:
        process_entry(entry, output_dir, mapped_file)

if __name__ == "__main__":
    # delete_all_pages()
    main()
