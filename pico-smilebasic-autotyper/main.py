# Raspberry Pi Pico / RP2040 SmileBASIC AutoTyper
# MicroPython 1.29+ recommended.
#
# Behavior:
# - registers as a USB HID keyboard
# - loads FILE_NAME into RAM
# - validates all characters before doing anything
# - waits for one BOOTSEL press
# - waits START_DELAY_MS
# - types the file exactly (CR is ignored, LF becomes Enter)
# - returns to waiting; BOOTSEL can be pressed again to retype
#
# Requires official MicroPython package:
#   usb-device-keyboard

import time
import rp2
from machine import Pin
import usb.device
from usb.device.keyboard import KeyboardInterface, KeyCode as KC

from settings import (
    FILE_NAME,
    START_DELAY_MS,
    KEY_HOLD_MS,
    CHAR_DELAY_MS,
    LINE_DELAY_MS,
)

LED = Pin(25, Pin.OUT)

SHIFT = KC.LEFT_SHIFT

_letter = {chr(ord("a") + i): getattr(KC, chr(ord("A") + i)) for i in range(26)}
_digit = {
    "1": KC.N1, "2": KC.N2, "3": KC.N3, "4": KC.N4, "5": KC.N5,
    "6": KC.N6, "7": KC.N7, "8": KC.N8, "9": KC.N9, "0": KC.N0,
}

_plain = {
    " ": KC.SPACE,
    "-": KC.MINUS,
    "=": KC.EQUAL,
    "[": KC.OPEN_BRACKET,
    "]": KC.CLOSE_BRACKET,
    "\\": KC.BACKSLASH,
    ";": KC.SEMICOLON,
    "'": KC.QUOTE,
    "\x60": KC.GRAVE,
    ",": KC.COMMA,
    ".": KC.DOT,
    "/": KC.SLASH,
    "\t": KC.TAB,
}

_shifted = {
    "!": KC.N1,
    "@": KC.N2,
    "#": KC.N3,
    "$": KC.N4,
    "%": KC.N5,
    "^": KC.N6,
    "&": KC.N7,
    "*": KC.N8,
    "(": KC.N9,
    ")": KC.N0,
    "_": KC.MINUS,
    "+": KC.EQUAL,
    "{": KC.OPEN_BRACKET,
    "}": KC.CLOSE_BRACKET,
    "|": KC.BACKSLASH,
    ":": KC.SEMICOLON,
    '"': KC.QUOTE,
    "~": KC.GRAVE,
    "<": KC.COMMA,
    ">": KC.DOT,
    "?": KC.SLASH,
}


def keys_for_char(ch):
    if ch == "\n":
        return (KC.ENTER,)
    if ch == "\r":
        return None
    if ch in _letter:
        return (_letter[ch],)
    low = ch.lower()
    if "A" <= ch <= "Z" and low in _letter:
        return (SHIFT, _letter[low])
    if ch in _digit:
        return (_digit[ch],)
    if ch in _plain:
        return (_plain[ch],)
    if ch in _shifted:
        return (SHIFT, _shifted[ch])
    raise ValueError("Unsupported character: %r (U+%04X)" % (ch, ord(ch)))


def load_and_validate():
    with open(FILE_NAME, "r") as f:
        text = f.read()

    for index, ch in enumerate(text):
        try:
            keys_for_char(ch)
        except ValueError as exc:
            raise ValueError("At character %d: %s" % (index, exc))

    return text


def wait_keyboard_ready(kbd):
    while not kbd.is_open():
        LED.value(0)
        time.sleep_ms(100)
    LED.value(1)


def wait_send_ready(kbd):
    while kbd.busy():
        time.sleep_ms(2)


def tap(kbd, keys):
    if keys is None:
        return

    wait_send_ready(kbd)
    kbd.send_keys(keys)
    time.sleep_ms(KEY_HOLD_MS)

    wait_send_ready(kbd)
    kbd.send_keys(())

    if keys == (KC.ENTER,):
        time.sleep_ms(LINE_DELAY_MS)
    else:
        time.sleep_ms(CHAR_DELAY_MS)


def wait_for_bootsel_press():
    while rp2.bootsel_button():
        time.sleep_ms(30)

    while not rp2.bootsel_button():
        time.sleep_ms(30)

    time.sleep_ms(50)
    while rp2.bootsel_button():
        time.sleep_ms(30)


def countdown():
    seconds = max(0, START_DELAY_MS // 1000)
    remainder = max(0, START_DELAY_MS - seconds * 1000)

    for _ in range(seconds):
        LED.value(0)
        time.sleep_ms(150)
        LED.value(1)
        time.sleep_ms(850)

    if remainder:
        time.sleep_ms(remainder)


def type_text(kbd, text):
    LED.value(1)
    for ch in text:
        tap(kbd, keys_for_char(ch))


def done_blink():
    for _ in range(3):
        LED.value(0)
        time.sleep_ms(150)
        LED.value(1)
        time.sleep_ms(150)


def main():
    LED.value(0)

    text = load_and_validate()

    keyboard = KeyboardInterface()
    usb.device.get().init(keyboard, builtin_driver=True)
    wait_keyboard_ready(keyboard)

    while True:
        wait_for_bootsel_press()
        countdown()
        type_text(keyboard, text)
        done_blink()


main()
