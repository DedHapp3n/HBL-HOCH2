# Pico SmileBASIC AutoTyper

A small USB-HID auto-typing helper for **Raspberry Pi Pico (RP2040)**.

It was made to enter long SmileBASIC source files without typing them by hand.

## What it does

- The Pico appears as a USB keyboard.
- It does **not** start typing immediately.
- Press **BOOTSEL once** to arm it.
- It waits 5 seconds.
- It types the complete contents of `bootstrap.txt`.
- After finishing, it waits for BOOTSEL again.

To type a different payload later, replace only `bootstrap.txt`. The Pico code does not need to change.

## Hardware

- Raspberry Pi Pico / RP2040
- Data-capable Micro-USB cable
- Nintendo Switch / Switch 2
- SmileBASIC 4

## Important: keyboard layout

The HID map in this project is **US / English 101/104-key layout**.

On the Switch, set the USB keyboard layout to **English** before using the Pico.

**Important:** SmileBASIC caches the keyboard layout when it starts. If you change the Switch USB keyboard layout while SmileBASIC is already open, completely restart SmileBASIC before testing again.

If the layout is wrong, symptoms include things such as:

- `Y` becoming `Z`
- `#` becoming `3`
- `$` becoming `4`
- shifted punctuation becoming incorrect characters

## MicroPython setup

Use a recent stable MicroPython build for **Raspberry Pi Pico (RP2040)**.

1. Disconnect the Pico.
2. Hold **BOOTSEL** while plugging it into the PC.
3. Copy the MicroPython UF2 to the `RPI-RP2` drive.
4. Install the MicroPython USB keyboard package:

```bash
py -m pip install -U mpremote
py -m mpremote mip install usb-device-keyboard
```

5. Copy the project files to the Pico:

```bash
py -m mpremote fs cp settings.py :settings.py
py -m mpremote fs cp bootstrap.txt :bootstrap.txt
py -m mpremote fs cp main.py :main.py
py -m mpremote reset
```

## Usage

1. Set the Switch USB keyboard layout to **English**.
2. Restart SmileBASIC after changing the layout.
3. Open **Make a Program**.
4. Open an empty slot and place the cursor at the first character of the first line.
5. Connect the Pico to the Switch.
6. Wait briefly for the keyboard to enumerate.
7. Press **BOOTSEL once** and release it.
8. The Pico waits 5 seconds, then types `bootstrap.txt` line by line.
9. The Pico LED blinks three times when typing is complete.
10. Save the program in SmileBASIC as required (for ns2jb: `NS2`).

Press BOOTSEL again to type the file again.

## Timing

Edit `settings.py`:

```python
START_DELAY_MS = 5000
KEY_HOLD_MS = 12
CHAR_DELAY_MS = 20
LINE_DELAY_MS = 120
```

If SmileBASIC misses characters, increase `CHAR_DELAY_MS` and/or `LINE_DELAY_MS`.

## Changing the typed text

Edit or replace `bootstrap.txt`, then copy it back to the Pico:

```bash
py -m mpremote fs cp bootstrap.txt :bootstrap.txt
py -m mpremote reset
```

No change to `main.py` is required.

## Validation

Before copying a new text file to the Pico, run:

```bash
python validate_payload.py
```

The validator checks whether every character is supported by the current US HID mapping.

## Notes

- BOOTSEL during normal runtime is used as the start button.
- Holding BOOTSEL while plugging the Pico into USB enters the RP2040 bootloader instead.
- The file is loaded into RAM before BOOTSEL polling starts.
- Windows CRLF text is handled correctly: CR is ignored and LF becomes Enter.
