#!/usr/bin/env python3
"""Entry for make.fun news-image-01: sum up 13 November 2026 world news in one image.

The image (entry.png, JPEG bytes, 1024x1024, <1 MiB) is a newspaper front
page for Friday 13 November 2026, built from that day's reported news:
Ukraine's ~1,200-drone attack and Europe joining peace talks; the US
downing two Iranian drones bound for Bahrain, Iran's radar-strike claim and
four tankers hit in the Strait of Hormuz; Nvidia chief Jensen Huang
resigning; the global Microsoft 365 outage entering its second day; the FAA
lifting its nationwide ground stop; China's unannounced Pacific drills
around Taiwan; the IEA oil-surplus forecast; and the Brooklyn collapse toll
reaching eight. The program copies it to /output/entry.png (or
$MAKEFUN_OUTPUT_DIR/entry.png). Deterministic: same input bytes always
produce the same output bytes. No network, stdlib only.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, os.path.join(OUT_DIR, "entry.png"))
