
## Tìm hiểu về giải pháp theo dõi hệ thống Zabbix

## 1. Mở đầu về Zabbix

- Zabbix là giải pháp giám sát phân tán mã nguồn mở. Cha đẻ của Zabbix là Alexei Vladishev, và hiện tại được phát triển và hỗ trợ bởi Zabbix SIA
- Zabbix được sủ dụng để giám sát nhiều thông số liên quan đến network, tình trạng sức khỏe của các thiết bị và khả năng đáp ứng của các máy chủ. Zabbix cung cấp cơ chế xây dựng hệ thông thông báo linh hoạt cho phép người dùng cấu hình các hệ thống email alert trên mọi event bất kỳ. Điều này giúp người quản trị tiếp cận với lỗi sớm nhất. Zabbix cũng cung cấp các hệ thống report và visualisation
- Zabbix hỗ trợ báo cáo và số liệu thống kê và cung cấp giao diện web cho người quản trị dễ dàng quản trị. Với web-base người quản trị có thể theo dõi trạng thái của network và server có thể truy cập từ bất cứ nơi nào . Việc kết hợp các chức năng trên Zabbix đúng tổ chức sẽ giúp xây dựng một nền tảng theo dõi hạ tầng Công Nghệ Thông Tin
- Zabbix là một dự án hoàn toàn miễn phí và được phân phối dưới giấy phép General Public License version 2.

## 2. Chức năng trong Zabbix 

- Zabbix cung cấp hàng loạt chức năng trong một package

### 2.1. Thu nhập dữ liệu 
- kiểm tra tính sẵn sàng và hiệu suất
- hỗ trợ các chức năng  SNMP, IPMI, JMX  và theo dõi VMware 
- xây dựng các lệnh kiểm tra tùy ý
- thu nhập dữ liệu theo thời gian định kỳ
- được thực hiện bởi các agent hoặc proxy

### 2.2. Định nghĩa các ngưỡng linh hoạt 
- xác định các ngưỡng của các lỗi trên hệ thống một cách linh hoạt 


### 2.3. Hệ thống cảnh báo 

- Cấu hình tùy chọn cảnh báo theo yêu cầu 

### 2.4.Real-time graphing

- Chức năng vẽ biểu đồ theo thời gian thực cho các ứng dụng 


### 2.5.Web monitoring capabilities

- Kiểm tra khả năng phản hồi của các Website dưới góc độ  trải nghiệm của người dùng 

### 2.6.Extensive visualisation options

- Khả năng xây dựng các biểu đồ trực quan 

### 2.7.Historical data storage

- Khă năng lưu dữ dữ liệu lâu dài trong các hệ cơ sở dữ liệu 
    
### 2.8.Easy configuration

- Cấu hình dễ dàng , khả năng pick up dễ dàng 

### 2.9. Zabbix features 

-  Khả năng sử  dụng các template cho các host 

### 2.10 Network discovery

- Khả năng discovery các nework device 


### 2.11. Fast web interface

- Khả năng truy cập vào hệ  thống qua web dashboard
- Có thể truy cập mọi nơi, mọi thời điểm và đảm bảo bảo mật 

### 2.12. Zabbix API

- Cung cấp các API cho các phần mềm thứ 3


### 2.3. Permissions system

- Hệ thống bảo mật, xác thực chặt chẽ.



## 3. Các thành phần trong Zabbix


### 3.1. Server 

- Zabbix Server là trung tâm, core của cả hệ thống Zabbix
- Server thực hiện pooling các dữ liệu, tính toán các thông số để gửi các thông báo. Phần trung tâm này đảm nhiệm là điểm chính cho các agent và proxy report các dữ liệu về khả năng của hệ thống. hoặc có thể chủ động kiểm tra các network service.
- Server sẽ chwacs toàn bộ cấu hình, dữ liệu và tạo dựng bởi 3 thành phần chính :  Zabbix server, web frontend and database storage.


### 3.2. Agent

- Các agent được cài đặt trên các các chủ đích cần theo dõi các tài nguyên và ứng dụng trên đó. 
- Các agent này đảm nhiểm collect các thống số dựa theo yêu cầu từ server, sau đó sẽ report về server.

- Agent được chia thành 2 trường phái :
    - Passive check : server sẽ hỏi các metric và agent sẽ gửi các metric tương ứng về
    - Active check :  Agent sẽ chủ động gửi request đến Zabbix Server nhằm lấy thông tin về các Item được Server chỉ định sẵn. Sau khi lấy được danh sách item thì Agent sẽ xử lý động lập rồi gửi tuần tự thông tin về cho Server. 

### 3.3. Zabbix proxy

- Được hiểu như một trung tâp thu nhập metric, thay vì dữ liệu được hàng loạt device và host gửi về trực tiếp Server thì sẽ được gửi đến Proxy này. 
- Hàng loạt dữ liệu từ các host và device sẽ được proxy thay mặt Zabbix Server đảm nhận thuy nhập và gửi lại về cho Server.


### 3.5. Zabbix sender 

- Bộ command line được sử dụng để gửi các metric data về Server để xử lý


### 3.6. Zabbix get

- Bộ command lien được sử dụng để làm việc với zabbix agent để nhận các metric từ agent. 