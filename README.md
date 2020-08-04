# Archived

This project did not satisfy my requirements in the end, and I have decided to archive it.

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

## Pi Setup As Tested

- Setup: https://www.raspberrypi.org/downloads/
- Add `ssh` file to the boot partition of the SD card to enable remote
- Add `dtoverlay=disable-wifi` and `dtoverlay=disable-bt` to the boot `config.txt` if you do not want the radios enabled
- SSH into the Pi with user `pi` password `raspberry`
- Use `passwd` to change password
- `sudo rm /etc/xdg/autostart/piwiz.desktop` to disable the setup wizard

Setup the case LCD if you have one:
```
git clone https://github.com/goodtft/LCD-show.git
cd  LCD-show/
sudo  ./MHS35-show
```

```
sudo apt-get update
sudo apt-get remove geany thonny vlc gpicview chromium-browser realvnc-vnc-server
sudo apt-get autoremove
sudo apt-get dist-upgrade
sudo apt-get autoremove
sudo apt-get install exfat-fuse exfat-utils vim
git clone https://github.com/rmcauley/gopro-picopy.git
cd gopro-picopy
python3 -m pip install -r requirements.txt
mkdir -p ~/.config/pcmanfm/LXDE-pi
cp pcmanfm.conf ~/.config/pcmanfm/LXDE-pi/
chmod u+x copy.sh
cd ~/Desktop
ln -s ~/gopro-picopy/copy.sh
```
