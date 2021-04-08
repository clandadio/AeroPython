#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; Chris Landadio
; functioning as of 4/7/21

1::
Run pythonw MP_GUI_Glider_v1.py
Return

2::
Run pythonw MP_GUI_Payload_v1.py
Return

^c::
Run python MP_GUI_CameraSwitch_v1.py
Return

^d::
Run python
; test case for debugging
