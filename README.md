# pi-flick-volume-adjuster

## setup for pi with systemd

Change working directory in `winvolume.service`

```
# running
systemctl start winvolume.service

# start on boot
systemctl enable winvolume.service

# stop
systemctl stop winvolume.service

```
