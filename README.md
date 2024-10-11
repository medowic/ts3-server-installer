# ts3-server-installer
**Automatic TeamSpeak server installer for Windows and Linux**

> [!NOTE]
> Настройку и документацию этого софта на русском языке смотрите [здесь](docs/README_ru.md)

## Installing
### Windows
1. Download `ts3-installer-win.exe` from [releases](https://github.com/medowic/ts3-server-installer/releases)
2. Move `ts3-installer-win.exe` in anywhere you need and open it
3. Open `ts3server.exe`

You also can clone this repository and run `main.py` using `python` on your Windows PC

> [!NOTE]
> After installation, you should always open `ts3server.exe`. The server will be minimized to the system tray, where you can close it by **RMB (click on the TS3Server icon) -> Exit**

### Linux
> [!IMPORTANT]
> Make sure that `python3` is installed on your server

1. Run this commands:

```sh
git clone https://github.com/medowic/ts3-server-installer.git
cd ts3-server-installer
sudo bash ts3-installer.sh
```

2. After installation you can start and stop server by this commands:

```sh
systemctl start teamspeak # starting server
systemctl stop teamspeak # stopping server
```

You also can remove server from autostart:
```sh
systemctl disable teamspeak
```

## Usage
### Direct connection to the server
If you using direct connection to your server, you must have **public** (white) IP address

**You can connect by only IP without port**

> [!IMPORTANT]
> To run TeamSpeak Server, you must open these ports in your firewall or router (standard ports):
> ```
> 9937 (UDP)
> 30033 (TCP)
> ```

### VPN-services (Hamachi, Radmin and etc)
This way doesn't require a public IP. So, if you haven't it, you can use this way. Using VPN like these, you must make network in app, know your IP **in app** and connect by it.

We're recommend to use [Radmin](https://www.radmin-vpn.com/) for Windows and [Hamachi](https://www.vpn.net) for Linux

**You also can connect by only IP without port**

## License
This project is under the [MIT License](https://raw.githubusercontent.com/medowic/ts3-server-installer/master/LICENSE)
