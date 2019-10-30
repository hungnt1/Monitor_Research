


## 1. Lỗi : "Received empty response from Zabbix Agent at [192.168.100.xx]. Assuming that agent dropped connection because of access permissions."

- Trong trường hợp xuất hiện lỗi "Received empty response from Zabbix Agent at [192.168.100.32]. Assuming that agent dropped connection because of access permissions.", trong trường hợp để Zabbix Server có thể liên hệ tới máy Zabbix Agent phải trải qua NAT. Cần thực hiện chỉ rõ Gateway IP cho Zabbix Server hay là thiết bị định tuyến để đến được Zabbix Server trên các Zabbix Agent 

- Ví dụ trên Zabbix Agent, địa chỉ của Zabbix Server là `192.168.30.194`, và Zabbix Server đang đứng sau thiết bị định tuyến thực hiện NAT 192.168.100.33. cấu hình như sau 
```
vi /etc/zabbix/zabbix_agentd.conf

Server=192.168.30.194,192.168.100.33

```
