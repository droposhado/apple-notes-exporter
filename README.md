# apple-notes-exporter-draft

The Apple Notes application does not have an option to export all notes, only one by one in text or pdf,
this project export notes from Apple Notes app using Apple Script and converts to json format using Python.

Developed with:

* macOS Catalina 10.15
* Script Editor 2.11 (208)
* AppleScript 2.7
* Apple Notes 4.7 (1111.23)
* Python 3.9.0 via pyenv

## Limitations

* Not export attachments
* Not export body of locked notes (encrypted notes)
* Does not export notes from the *Recently Deleted* folder, this folder may change name depending on the language your system is used and only the english version of the name works.

## Separator!?

Yes, i know that my code (Apple Script) is not the best, but it was the simplest i got, i know more python and i left the processing in this language to make it easier for me and finish it soon. 

## Why did you create this code if there are already ready codes in the references?

These codes did not work on my macOS, however i observed them and built based on them.

What happens is that i disabled sync, then enabled it again and also created a local account and by default the account is "**iCloud**", so some code didn't work, so in the code there's the line `tell account "iCloud"`, to tell the Notes app what it counts to get my notes.

## How to use

Execute command in terminal

```
$ osascript notes.applescript > notes.txt
```

This generates a file called notes.txt, with format:

```
<SEPARATOR>folder_name           
note_name
note_creation_date
note_modification_date
note_password_protected       
note_plaintext
```

* `note_plaintext` contains the body of the note and is available from line 6 to the next

To convert to json format run the command:

```
$ mkdir dist
$ python notes.py
```

The command generates a folder called `dist`, with the file serialized, the name is generated based on UUID (`<uuid>.json`). Example json generated is:

```json
{
    "body": "content\nother content",
    "creation_date": "2013-02-10T12:56:13Z",
    "folder": "markdown",
    "id": "b3d8a851-3b63-445a-beba-fd905a2b30bf",
    "modification_date": "2013-02-12T00:43:44Z"
}
```

Or use:

```
$ make
```

## References

* [Scripting Notes: The Note Class](https://www.macosxautomation.com/applescript/notes/04.html)
* [https://github.com/robertgaal/notes-export](https://github.com/robertgaal/notes-export)
* [https://github.com/ayman/emacs-applenotes/blob/master/applenotes.el](https://github.com/ayman/emacs-applenotes/blob/master/applenotes.el) (based on `applenotes--get-notes-list`)

