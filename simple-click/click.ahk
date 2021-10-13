#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

^+C::
Loop {
    Click
    MouseGetPos, xpos, ypos
    Sleep, 500
    MouseGetPos, xpos2, ypos2
    If (xpos!=xpos2 || ypos!=ypos2) {
        Break
    }
}
return

+LButton::
    Loop
    {
        If !GetKeyState("LButton", "P")
        {
            Send {LButton Up}
            Break
        }

        Send {LButton Up}
        Send {LButton Down}
    }
return