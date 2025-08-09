# Daily Verse Python

https://github.com/user-attachments/assets/c8dcbb0d-e4f8-4063-bbad-7298e8211623

Verse catalogue taken from <https://git.vdm.dev/christian/daily-scripture>

`run.py` is your main module

## Example Waybar Config

```json
{
  ...
  "modules-center": ["custom/verse"],

  "custom/verse": {
    "return-type": "json",
    "format": "{}",
    "exec-on-event": false,
    "on-click": "pkill -SIGRTMIN+10 waybar",
    "signal": 10,
    "exec": "python ~/.local/bin/daily_verse/run.py"
  }
  ...
}
```
