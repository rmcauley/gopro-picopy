# gopro-picopy

Copies GoPro movies and images to the largest attached drive.  Meant to be used on Raspberry Pis as a lightweight portable method of backing up MicroSD cards used on GoPros to larger disks for those longer trips when you don't want to haul a laptop to do the job, or if you're wary of paying more for all-in-one devices.

## What does it do?

- Finds the smallest mounted disk that has a `DCIM/GOPRO100` directory
- Starts copying MP4, JPG, and JPEG files to the largest connected drive (not the internal MicroSD card)
- SHA256 verifies each file after copying for integrity

## What doesn't it do?

- Run automatically on device mount (you will need a way to start the script on the Pi yourself)
- Delete files (format the card on your GoPro once satisfied with the copy results)
- Show file copy progress

## What do I need on my Pi?

```
sudo apt-get install exfat-fuse exfat-utils
pip install -f requirements.txt
```
