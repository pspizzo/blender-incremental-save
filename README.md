# Incremental Saves

Save your blend files with an incrementing version number.

Use this add-on to make it easier to incrementally save your work. Instead of the cumbersome method of choosing "Save as...", moving your mouse over the filename and pressing the + key, and then clicking the confirming "Save As" button, now you can simply press Shift-Ctrl-S. Blender will save your file with a new, incremented version number.


## Installing in Blender

1. Download the IncrementalSave.py file or the full repository as a zip file.
2. In Blender, go to Edit->Preferences and select the "Add-Ons" section.
3. Press the "Install" button.
4. Select the IncrementalSave.py or the repository zip file. Now the add-on should be installed, but not enabled.
5. In the same view, find the installed "Incremental Saves" add-on (if not already shown).
6. Enable the add-on.


## Shortcut Key: Shift-Ctrl-S

- This add-on overrides the "Save As" hotkey. If you want to keep Shift-Ctrl-S for "Save As", edit the keymap in IncrementalSave.py to your desired shortcut before you load the add-on into Blender.
- When you disable or uninstall this add-on, the "Save As" shortcut will work as normal again.


## Behavior:
- If the file has not been saved yet, the standard "Save as" dialog appears.
- If the current filename does not end with a number, a "_v001" suffix is added to the main filename. Example:
  - "my_file.blend" -> "my_file_v001.blend".
- If the file ends with numbers, the number is incremented. The add-on attempts to preserve leading zeros. Examples:
  - "my_file_9.blend" -> "my_file_10.blend" 
  - "my_file_002.blend" -> "my_file_003.blend"
