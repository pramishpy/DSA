from __future__ import annotations
import sys
from typing import Callable, Dict, Tuple

#!/usr/bin/env python3
"""
units_facts.py

Simple unit conversion utility.
Supports: length, mass, temperature, volume, speed.
Usage:
    python units_facts.py [value] [from_unit] [to_unit]
Examples:
    python units_facts.py 10 km mi
    python units_facts.py            -> starts interactive REPL
"""


# Conversion tables to base units (SI): meters, kilograms, liters, m/s
_LENGTH_TO_M = {
    "m": 1.0,
    "meter": 1.0, "meters": 1.0,
    "km": 1000.0, "kilometer": 1000.0, "kilometers": 1000.0,
    "cm": 0.01, "centimeter": 0.01,
    "mm": 0.001, "millimeter": 0.001,
    "in": 0.0254, "inch": 0.0254, "inches": 0.0254,
    "ft": 0.3048, "foot": 0.3048, "feet": 0.3048,
    "yd": 0.9144, "yard": 0.9144,
    "mi": 1609.344, "mile": 1609.344,
}

_MASS_TO_KG = {
    "kg": 1.0, "kilogram": 1.0, "kilograms": 1.0,
    "g": 0.001, "gram": 0.001,
    "mg": 1e-6, "milligram": 1e-6,
    "lb": 0.45359237, "pound": 0.45359237, "pounds": 0.45359237,
    "oz": 0.028349523125, "ounce": 0.028349523125,
}

_VOLUME_TO_L = {
    "l": 1.0, "liter": 1.0, "litre": 1.0, "liters": 1.0,
    "ml": 0.001, "milliliter": 0.001,
    "m3": 1000.0, "m^3": 1000.0, "cubic_meter": 1000.0,
    "gal": 3.785411784, "gallon": 3.785411784,  # US liquid gallon
    "cup": 0.2365882365, "cups": 0.2365882365,
}

_SPEED_TO_MS = {
    "m/s": 1.0, "mps": 1.0, "meter/second": 1.0,
    "km/h": 1000.0 / 3600.0, "kph": 1000.0 / 3600.0,
    "mph": 1609.344 / 3600.0,
    "knot": 1852.0 / 3600.0, "kn": 1852.0 / 3600.0,
}

# Temperature conversions handled separately
_TEMP_UNITS = {"c", "celsius", "f", "fahrenheit", "k", "kelvin"}


def _normalize(unit: str) -> str:
    return unit.strip().lower()


def _convert_linear(value: float, from_unit: str, to_unit: str,
                    table_from: Dict[str, float], table_to: Dict[str, float]) -> float:
    f = table_from.get(from_unit)
    t = table_to.get(to_unit)
    if f is None or t is None:
        raise ValueError("unit not supported for this category")
    # convert from -> base -> to
    base = value * f
    return base / t


def _convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    fu = from_unit
    tu = to_unit

    def to_c(v: float, u: str) -> float:
        if u in ("c", "celsius"):
            return v
        if u in ("f", "fahrenheit"):
            return (v - 32.0) * 5.0 / 9.0
        if u in ("k", "kelvin"):
            return v - 273.15
        raise ValueError("unknown temperature unit")

    def from_c(v: float, u: str) -> float:
        if u in ("c", "celsius"):
            return v
        if u in ("f", "fahrenheit"):
            return v * 9.0 / 5.0 + 32.0
        if u in ("k", "kelvin"):
            return v + 273.15
        raise ValueError("unknown temperature unit")

    c = to_c(value, fu)
    return from_c(c, tu)


def convert(value: float, from_unit: str, to_unit: str) -> float:
    fu = _normalize(from_unit)
    tu = _normalize(to_unit)

    # temperature
    if fu in _TEMP_UNITS and tu in _TEMP_UNITS:
        return _convert_temperature(value, fu, tu)

    # length
    if fu in _LENGTH_TO_M and tu in _LENGTH_TO_M:
        return _convert_linear(value, fu, tu, _LENGTH_TO_M, _LENGTH_TO_M)

    # mass
    if fu in _MASS_TO_KG and tu in _MASS_TO_KG:
        return _convert_linear(value, fu, tu, _MASS_TO_KG, _MASS_TO_KG)

    # volume
    if fu in _VOLUME_TO_L and tu in _VOLUME_TO_L:
        return _convert_linear(value, fu, tu, _VOLUME_TO_L, _VOLUME_TO_L)

    # speed
    if fu in _SPEED_TO_MS and tu in _SPEED_TO_MS:
        return _convert_linear(value, fu, tu, _SPEED_TO_MS, _SPEED_TO_MS)

    raise ValueError(f"Conversion from '{from_unit}' to '{to_unit}' not supported.")


def _format_result(value: float) -> str:
    # choose formatting: if near-integer, show integer
    if abs(value - round(value)) < 1e-9:
        return str(int(round(value)))
    # otherwise use up to 8 significant digits
    return ("{:.8g}").format(value)


def _print_help() -> None:
    print(__doc__)
    print("Supported examples of units:")
    print("  length: m, km, cm, mm, in, ft, yd, mi")
    print("  mass: kg, g, mg, lb, oz")
    print("  temperature: C, F, K")
    print("  volume: L, mL, m3, gal, cup")
    print("  speed: m/s, km/h, mph, knot")
    print("Examples:")
    print("  convert 10 km mi")
    print("  convert 100 F C")


def _repl() -> None:
    print("units_facts REPL. Type 'help' or 'quit'.")
    try:
        while True:
            line = input("> ").strip()
            if not line:
                continue
            if line.lower() in ("quit", "exit"):
                break
            if line.lower() in ("help", "h", "?"):
                _print_help()
                continue
            parts = line.split()
            if len(parts) < 3:
                print("Enter: value from_unit to_unit")
                continue
            try:
                val = float(parts[0])
            except ValueError:
                print("Invalid numeric value.")
                continue
            from_u = parts[1]
            to_u = parts[2]
            try:
                res = convert(val, from_u, to_u)
                print(f"{_format_result(res)} {to_u}")
            except Exception as e:
                print("Error:", e)
    except (EOFError, KeyboardInterrupt):
        print()


def _main(argv) -> None:
    if len(argv) == 1:
        _repl()
        return
    if argv[1] in ("-h", "--help", "help"):
        _print_help()
        return
    if len(argv) < 4:
        print("Usage: python units_facts.py [value] [from_unit] [to_unit]")
        print("Try 'python units_facts.py' for interactive mode.")
        return
    try:
        val = float(argv[1])
    except ValueError:
        print("First argument must be a number.")
        return
    from_u = argv[2]
    to_u = argv[3]
    try:
        res = convert(val, from_u, to_u)
        print(_format_result(res))
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    _main(sys.argv)