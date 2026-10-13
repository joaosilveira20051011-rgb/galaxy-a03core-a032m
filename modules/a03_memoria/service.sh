#!/system/bin/sh
i=0
while [ "$(getprop sys.boot_completed)" != "1" ]; do
    i=$((i + 1))
    [ "$i" -ge 180 ] && exit 1
    sleep 2
done
sleep 5
echo 70 > /proc/sys/vm/swappiness
echo 1 > /proc/sys/vm/page-cluster
echo 5 > /proc/sys/vm/watermark_scale_factor
