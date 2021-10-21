all: text json

EXP_FILENAME=notes.txt

text:
	osascript notes.applescript > $(EXP_FILENAME)

json:
	rm -rf dist
	mkdir dist
	python notes.py $(EXP_FILENAME)
