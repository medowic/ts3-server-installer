# ts3-server-installer
**Авто-установщик TeamSpeak Server для Windows и Linux**

## Установка
### Windows
1. Скачайте `ts3-installer-win.exe` из [releases](https://github.com/medowic/ts3-server-installer/releases)
2. Переместите файл `ts3-installer-win.exe` туда, где будет располагаться сервер и запустите его
3. Откройте `ts3server.exe`

Вы также можете клонировать этот репозиторий и запустить `main.py` используя `python` на Windows

> [!NOTE]
> После установки всегда запускайте файл `ts3server.exe`. Сервер будет свёрнут в трей. Закрыть его можно при помощи ПКМ (по иконке TS3Server) -> Exit

### Linux
> [!IMPORTANT]
> Убедитесь, что `python3` установлен на сервере

1. Введите и запустите эти команды:

```sh
git clone https://github.com/medowic/ts3-server-installer.git
cd ts3-server-installer
sudo bash ts3-installer.sh
```

2. После установки вы можете запускать и останавливать сервер при помощи этих команд:

```sh
systemctl start teamspeak # запуск сервера
systemctl stop teamspeak # остановка сервера
```

Вы также можете убрать сервер из автозагрузки:
```sh
systemctl disable teamspeak
```

## Использование
### Прямое подключение к серверу

Используя этот способ, вы должны иметь публичный (белый) айпи-адрес. Узнать его можно [здесь](https://icanhazip.com/).


**Вы сможете подключиться используя только айпи-адрес без порта**

> [!IMPORTANT]
> Чтобы TeamSpeak Server заработал, вы должны открыть эти порты в настройках брандмауэра или роутера:
> ```
> 9937 (UDP)
> 30033 (TCP)
> 10011 (TCP)
> ```

### VPN-сервисы (Hamachi, Radmin и прочие)
Этот способ не требует публичного айпи-адреса. Так, если вы не имеете его, вы можете воспользоваться им. Используя эти VPN, вы должны создать сеть в приложении, узнать свой айпи **в приложении** и подключиться по нему.

Мы рекомендуем использовать [Radmin](https://www.radmin-vpn.com/) для Windows и [Hamachi](https://www.vpn.net) для Linux

**Вы сможете также подключиться используя только айпи-адрес без порта**

## Лицензия
Этот проект находится под [лицензией MIT](https://raw.githubusercontent.com/medowic/ts3-server-installer/master/LICENSE)
