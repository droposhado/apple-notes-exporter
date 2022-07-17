from datetime import datetime
import json
import os
import sys
import uuid


SEPARATOR='###|'

HERE=os.path.dirname(os.path.realpath(__file__))
OUTPUT=os.path.join(HERE, "dist")

# Example mask to parse:
# 12H time: `Friday, September 22, 2017 at 1:00:52 PM`
# 24H time: `Friday, September 22, 2017 at 13:00:52`
DATETIME_IMPORT_MASK_12H='%A, %B %d, %Y at %I:%M:%S %p'
DATETIME_IMPORT_MASK_24H='%A, %B %d, %Y at %H:%M:%S'
DATETIME_SAVE_MASK='%Y-%m-%dT%H:%M:%SZ'


def get_datetime_string(string):
    try:
        dt_obj = datetime.strptime(string, DATETIME_IMPORT_MASK_12H)
    except ValueError:
        # 24h time
        dt_obj = datetime.strptime(string, DATETIME_IMPORT_MASK_24H)

    return dt_obj.strftime(DATETIME_SAVE_MASK)


def get_bool(string):
    return True if string == "true" else False


filename = sys.argv[1]

file_exists = os.path.exists(filename)
if not file_exists:
    print('ERROR: file not exists')

with open(filename, mode='r') as file_raw:
    file = file_raw.read()
    notes = file.split(SEPARATOR)

    for note in notes:

        if note is None or note == '':
            continue

        properties = note.split('\n')

        folder_name = properties[0]
        note_name = properties[1]
        note_creation_date = properties[2]
        note_modification_date = properties[3]
        note_password_protected = get_bool(properties[4])
        note_plaintext = "\n".join(properties[5:-1])

        note_id = str(uuid.uuid4())
        note_json = {
            "id": note_id,
            "folder": folder_name,
            "creation_date": get_datetime_string(note_creation_date),
            "modification_date": get_datetime_string(note_modification_date),
            "body": note_plaintext
        }

        if note_password_protected:
            print("INFO: Note '{}' in folder '{}' is encrypted and cannot be exported".format(note_name, folder_name))

        file_export = os.path.join(OUTPUT, "{}.json".format(note_id))

        if os.path.exists(file_export):
            print('ERROR: UUID already in use')

        with open(file_export, mode='w') as f_e:
            f_e.seek(0)
            f_e.write(json.dumps(note_json, indent=4, separators=(',', ': '), sort_keys=True))

        print("EXPORTED: Folder '{}', note '{}'".format(folder_name, note_name))
