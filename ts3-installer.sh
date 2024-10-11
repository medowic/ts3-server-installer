#!/usr/bin/bash

if [ "${EUID}" -ne 0 ]; then
    echo "Error: Script must be start from root";
    exit 1;
fi

useradd -m -r -s /usr/sbin/nologin teamspeak
cp main.py /home/teamspeak
cd /home/teamspeak || { echo "Error: Couldn't change directory to '/home/teamspeak'"; exit 1; }

python3 main.py
EXITLVL="${?}"

if [ "${EXITLVL}" == "1" ]; then
    exit 1;
fi

chown -R teamspeak:teamspeak /home/teamspeak
chmod -R 700 /home/teamspeak

echo "[Unit]
Description=TeamSpeak3 Server
After=network.target

[Service]
WorkingDirectory=/home/teamspeak/ts3-server
User=teamspeak
Group=teamspeak
Type=forking
ExecStart=/home/teamspeak/ts3-server/ts3server_startscript.sh start inifile=ts3server.ini
ExecStop=/home/teamspeak/ts3-server/ts3server_startscript.sh stop
PIDFile=/home/teamspeak/ts3-server/ts3server.pid
RestartSec=25
Restart=always

[Install]
WantedBy=multi-user.target" | tee /lib/systemd/system/teamspeak.service >/dev/null 2>&1

systemctl daemon-reload
systemctl start teamspeak
systemctl enable teamspeak >/dev/null 2>&1

STOKEN="$(cat /home/teamspeak/ts3-server/logs/ts3server_* | grep -o 'token.*' | cut -f2- -d=)"
echo "Done! Installation was successful."
echo "Here's your server admin token: ${STOKEN}"
exit 0
