
## Hanoi, 30/10/2019


##  Chiêm nghiệm cá nhân : Sách nào cũng không bằng docs ở trang chủ, thế nên cứ theo flow của nó.


## Phiên bản tìm hiểu : CheckMK 1.6


## 1. checkmk là gì ?

- Theo ank Wiki, checkmk là một phần mềm được viết bằng Python và C++ nhằm mục đích giám sát hạ tầng công nghệ thông tin. CheckMK có thể giát  sát máy chủ, ứng dụng, hạ tầng mạng, container, hệ thống lưu trữ, cơ sỡ dữ liệu   và  điều kiện môi trường.


- ChecMK được khởi xướng vào 2008, base trên nền nagios core và bổ sung hoàng loạt các compoment mới. Edition Opensource của checkmk được tiếp tục phát triển dựa trên Nagios Core và bổ sung hoàng loạt các thành phần khác để xây dựng một hệ thống hoàn chỉnh. 

- Tuy nhiên, trong nhiều năm trong quá trình checmk phiên bản miễn phí vẫn được maintain thì các edtion hướng thương lại của checmk được phát triển. Các edtion hướng thương mại tự xây dựng một hệ thống giám sát của riêng họ, điểm nôi bật nhất ở đây là họ đã tự xây dựng core thay vì sử dụng Nagios Core như edition miễn phí. 

- CheckMK cung cấp 4 phiên bản khác nhau :
    - RAW edition : được cung cấp dưới dạng mã nguồn mở, miễn phí 100% 
    - Enterprise - Free edition : phiên bản doanh nghiệp dưới mạng miễn phí, hạn chế chỉ cho phép tối đa 10 host có thể giám sát đồng thời
    - Enterprise - Standard edition : phiên bản doanh nghiệp, mang xu hướng chuyên nghiệp và cung cấp các feature nâng cao,  cung cấp khả năng mở rộng hệ thống giám sát 
    - Enterprise - Managed Services edition : cung cấp phiên bản doanh nghiệp dưới dạng managed services. 

## 2. CheckMK giám sát được gì ?

- Trang chủ của checkMK có liệt kê một số môi trường mà sản phẩm có thể theo dõi 
    - Giám sát máy chủ : Windows Server, Linux, Unix, RHEL, Centos, Debian, Virtual Machine ...
    - Giám sát ứng dụng : Apache, Nginx, Webphere, POSTfix ...
    - Giám sát mạng : Ciso, Dell, F5, HP, Huawei, IBM, Intel, Juniper  .... 
    - Giám sát điện toán đám mây : AWS S3, EC2,  AWS EBS, Azure ...
    - Giám sát lưu trữ : Dell, EMC, HP, IBM, NETAPP, Orcel, sao không thấy nhắc đến CEPH
    - Giám sát cơ sỡ dữ liệu : Mysql, Oracel, PostgreSQL, SQL, Azure SQL, MongoDB, 
    - Giám sát môi trường : cái này lạ, hỗ trợ lấy metric từ các thiết bị theo dõi nhiệt độ ẩm, nướ, điện, khói từ các hãng thiết bị APC, Bachmamn,  Wagner..
    - Giám sát Container : Docker và K8s

- Kho chứa hơn 1700 plugins


## 3. CheckMK cung cấp cái gì ?

- Dashboard  : checmk cung cấp Web-based Control, cho phép người dùng quản trị dễ dàng, cũng như xuất dữ liệu dưới dạng realtime
- Metric và Graphing : cung cấp khả năng phân tích metric dưới dạng time-series, cung cấp các graph HTML5
- Giám sát hạ tầng : Cung cấp khả năng giám sát host và service dưới dạng overview và deepdive
- Log và giám sát các event : thực hiện phân tích log và các event
- Tính toán SLA : khả năng cung cấp các report về SLA
- Thông báo và cảnh báo : cung cấp hệ thống rule-base notification ( trigger system )
- Cấu hình : cung cấp khả năng cấp hình tập trung và thông minh



