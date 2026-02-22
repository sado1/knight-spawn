# knight-spawn
Generates commands to spawn a server instance for Knights and Merchants: Remake or Knights Province.

# Example usage
```bash
$ ./main.py some_username https://release.xxx.xyz/KMR_linux_dedicated_servers_r12345_net_v12345.7z r12345 KMR 56789 '[$00ff00]Server name' '[$ff0000]Server description.'

apt update
apt install p7zip-full
useradd -m -d /home/some_username some_username
mkdir -p /home/some_username/r12345
cd /home/some_username/r12345
curl -L https://release.xxx.xyz/KMR_linux_dedicated_servers_r12345_net_v12345.7z -o KMR_linux_dedicated_servers_r12345_net_v12345.7z
7z x KMR_linux_dedicated_servers_r12345_net_v12345.7z
chmod +x KaM_Remake_Server_linux_x86_64
chown some_username:some_username -R /home/some_username/r12345
echo '[Unit]
Description=KaM Remake r12345 game server
After=network.target

[Service]
WorkingDirectory=/home/some_username/r12345
User=some_username
Group=some_username
Type=simple
ExecStart=/home/some_username/r12345/KaM_Remake_Server_linux_x86_64
RestartSec=15
Restart=always

[Install]
WantedBy=multi-user.target' > /usr/lib/systemd/system/KMR-r12345.service

chmod +x /usr/lib/systemd/system/KMR-r12345.service

systemctl start KMR-r12345.service; sleep 3; systemctl stop KMR-r12345.service
sed -i "s/ServerName=.*/ServerName='[\$00ff00]Server name'/g" "KaM Remake Server Settings.ini"
sed -i "s/WelcomeMessage=.*/WelcomeMessage=[\$ff0000]Server description./g" "KaM Remake Server Settings.ini"
sed -i "s/ServerPort=.*/ServerPort=56789/g" "KaM Remake Server Settings.ini"
sed -i "s/UDPScanPort=.*/UDPScanPort=56790/g" "KaM Remake Server Settings.ini"
rm KMR_linux_dedicated_servers_r12345_net_v12345.7z

# Done. Now test connectivity and remember to allow access to your port on firewalls.
```
