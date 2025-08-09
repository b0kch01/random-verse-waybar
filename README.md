# Daily Verse Python

Verse catalogue taken from <https://git.vdm.dev/christian/daily-scripture>

`run.py` is your main module

## Example Waybar Config:

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
