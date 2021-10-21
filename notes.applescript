-- https://www.macosxautomation.com/applescript/notes/04.html
-- https://github.com/robertgaal/notes-export
-- https://github.com/panicsteve/notes-import
-- https://github.com/ayman/emacs-applenotes/blob/master/applenotes.el based on applenotes--get-notes-list
-- https://gist.githubusercontent.com/drewdiver/740f6e78cc4ec20632b5d9c5fe8d1cda/raw/e055b0f49bf7661cce14efee6a69c8c5b5df1ba8/Generate%2520UUID%2520to%2520Clipboard.applescript

tell application "Notes"
	tell account "iCloud"
		
		activate

		set bodies to ""
		set separator to "###|"
		set linebreaker to "
"

		repeat with folder_obj in every folder
			
			set folder_name to name of folder_obj
			
			set folder_notes to notes of folder_obj
			
			
			if folder_name is not "Recently Deleted" and (count of the folder_notes) is not 0 then
				
				repeat with note_obj in notes of folder_obj
					
					set note_name to name of note_obj
					set note_id to id of note_obj
					set note_container_obj to container of note_obj
					set note_body to body of note_obj
					set note_plaintext to plaintext of note_obj
					set note_creation_date to creation date of note_obj
					set note_modification_date to modification date of note_obj
					set note_password_protected to password protected of note_obj
					
					set bodies to bodies & separator
					
					set bodies to bodies & folder_name & linebreaker
					
					set bodies to bodies & note_name & linebreaker
					
					-- container is folder name or folder representation, but 
					-- set bodies to bodies & container_name & linebreaker
					
					set bodies to bodies & note_creation_date & linebreaker
					set bodies to bodies & note_modification_date & linebreaker
					
					set bodies to bodies & note_password_protected & linebreaker
					
					set bodies to bodies & note_plaintext & linebreaker
					
				end repeat
			end if
			
		end repeat
		
		-- Send to default output
		return bodies
		
	end tell
end tell