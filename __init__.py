#
# Incremental Saves
# Save your blend files with an incrementing version number.
#
# Shortcut key: Shift-Ctrl-S
# * This overrides the "Save As" hotkey. If you want to keep Shift-Ctrl-S
#   for "Save As", edit the hotkey below to your desired shortcut before
#   you load the add-on into Blender.
# * When you disable or uninstall this add-on, the "Save As" shortcut will
#   work as normal again.
#
# Behavior:
# * If the file has not been saved yet, the standard "Save as" dialog appears.
# * If the current filename does not end with a number, a "_v001" suffix is
#   added to the main filename. Example: "my_file.blend" is saved as
#   "my_file_v001.blend".
# * If the file ends with numbers, the number is incremented. Leading zeros
#   are attempted to be preserved. Examples:
#   - "my_file_9.blend" -> "my_file_10.blend" 
#   - "my_file_002.blend" -> "my_file_003.blend"
#
#
#  MIT License
#
#  Copyright (c) 2021 Patrick Spizzo
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#

bl_info = {
    "name": "Incremental Saves",
    "description": "Save your blend files with an incrementing version number.",
    "author": "Patrick Spizzo",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "File > Save Incremental",
    "wiki_url": "https://github.com/pspizzo/blender-incremental-save",
    "category": "System",
}

from .IncrementalSaves import *
