echo "Copying files to their locations.."
cp readGPIO /usr/local/bin
cp readGPIO.cgi /usr/lib/cgi-bin
cp finalCGI.html /var/www/html

echo "Adding permissions..."
chmod 755 /usr/lib/cgi-bin/readGPIO.cgi
# Led must give others execute permissions
chmod 777 /sys/class/gpio/gpio60/*
chmod +s /usr/lib/cgi-bin/readGPIO.cgi

