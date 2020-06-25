import os
import psutil
import datetime
import shutil
import hashlib
from os import path

IGNORE_MOUNTPOINTS = ("/", "/boot")
COPY_FILENAMES = ("mp4", "jpg", "jpeg")

# taken from:  https://stackoverflow.com/a/44873382
def sha256sum(filename):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()

drives = sorted(
    [
        (p.mountpoint, psutil.disk_usage(p.mountpoint).total)
        for p in psutil.disk_partitions()
        if p.mountpoint not in IGNORE_MOUNTPOINTS
    ],
    key=lambda p: p[1],
)

source = os.path.join(next(
    (
        drive[0]
        for drive in drives
        if path.exists(path.join(drive[0], "DCIM", "100GOPRO"))
    ),
    None,
), "DCIM", "100GOPRO")
destination = path.join(drives[-1][0], datetime.datetime.now().strftime("%Y-%m-%d"))

try:
    os.mkdir(destination)
except FileExistsError:
    pass

print(f"Will copy from {source} to {destination}")

for _, _, files in os.walk(source):
    for filename in files:
        full_source = os.path.join(source, filename)
        full_destination = os.path.join(destination, filename)
        if filename.lower().split(".")[-1] in COPY_FILENAMES:
            source_sha = sha256sum(full_source)
            print(f"Copying {filename}")
            # copy2 preserves metadata
            shutil.copy2(full_source, full_destination)
            destination_sha = sha256sum(full_destination)
            if source_sha != destination_sha:
                raise ValueError(f"{filename} hash is different between source and destination.")

print("All done.")