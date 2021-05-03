#! /bin/sh
### BEGIN INIT INFO
# Provides: InternetOverUSB
# Required-Start: $all
# Required-Stop: $all
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: Enables Internet over USB cable
# Description: Enables access to the Internet over the Internet connection
# provided by the connected host
### END INIT INFO
case "$1" in
        start)
                sleep 20
                /root/bin/internetOverUSB
                /root/bin/StartSystem
        ;;
        stop)
                #no-op
        ;;
        *)
                #no-op
        ;;
esac
exit 0