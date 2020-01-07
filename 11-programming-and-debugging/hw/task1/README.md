# tcpdump и wireshark

1)Просмотр интерфейсов
```
			sudo tcpdump -D
```
2)Перехват всех запросов интерфейса lo
```
			sudo tcpdump -i lo
```
3) Забираем все, что приходит на локалхост, 3310 порт в pcap файл
```
	sudo tcpdump -i lo dst  127.0.0.1 and port 3310 -w mycap.pcap
```
