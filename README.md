# YSDA TLS client

Аналог nmap поверх Scapy. Сканирует занятые порты на хосте.

## Сборка и запуск окружения

1. Собираем conda:
```bash
conda create -n ysda-networks python scapy tqdm -y
```
2. Команда запуска:
```bash
conda activate ysda-networks
```

## Usage


Функциональность можно легко глянуть через `--help`:
```bash
$ python nmap.py -h                   
usage: nmap.py [-h] host ports

Nmap analogue.

positional arguments:
  host        destination host address
  ports       Ports range to scan, e.g. 1-100

options:
  -h, --help  show this help message and exit
```

### Пример

```bash
python nmap.py 10.0.0.1/24 8000-8004
```
