#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

+G::
Run C:\Users\kitty\AppData\Local\Programs\Python\Python39\pythonw H:\Aero\Python\MP_GUI_Glider_v1.py
Return

+H::
Run C:\Users\kitty\AppData\Local\Programs\Python\Python39\pythonw H:\Aero\Python\MP_GUI_Payload_v1.py
Return

+J::
Run C:\Users\kitty\AppData\Local\Programs\Python\Python39\python H:\Aero\Python\MP_GUI_CameraSwitch_v1.py
Return
