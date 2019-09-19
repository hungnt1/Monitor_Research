

## Openstack Resource Tracking


## 1. Kiểm tra process 

- Check nova prefix process 
```
[root@controller01 ~]# ps aux | grep nova-*
nova      1564  0.0  0.1 438012  8628 ?        Ss   Sep03   2:43 /usr/bin/python2 /usr/bin/nova-novncproxy --web /usr/share/novnc/
nova      1566  1.8  0.4 400652 28760 ?        Ss   Sep03  80:00 /usr/bin/python2 /usr/bin/nova-scheduler
nova      1591  0.2  1.5 402688 94040 ?        Ss   Sep03  10:35 /usr/bin/python2 /usr/bin/nova-consoleauth
nova      1592  1.8  0.4 397780 29008 ?        Ss   Sep03  80:06 /usr/bin/python2 /usr/bin/nova-conductor
nova      2771  0.7  1.8 422480 110996 ?       S    Sep03  29:38 /usr/bin/python2 /usr/bin/nova-conductor
nova      2772  0.7  1.8 421468 110240 ?       S    Sep03  29:35 /usr/bin/python2 /usr/bin/nova-conductor
root      3884  0.0  0.0 112712   992 pts/0    R+   10:22   0:00 grep --color=auto nova-*
nova      4112  0.1  1.5 403916 94024 ?        S    Sep03   7:50 /usr/bin/python2 /usr/bin/nova-scheduler
nova      4113  0.1  1.5 403960 93916 ?        S    Sep03   7:19 /usr/bin/python2 /usr/bin/nova-scheduler
nova      8117  0.1  1.8 689408 107892 ?       Sl   Sep05   1:13 /usr/sbin/httpd -DFOREGROUND
nova      8118  0.1  1.7 683264 101788 ?       Sl   Sep05   1:13 /usr/sbin/httpd -DFOREGROUND
nova      8119  0.1  1.7 685056 104016 ?       Sl   Sep05   1:12 /usr/sbin/httpd -DFOREGROUND
nova     11447  1.9  1.9 452684 118892 ?       Ss   Sep03  77:55 /usr/bin/python2 /usr/bin/nova-api
nova     11540  0.1  2.7 495256 164848 ?       S    Sep03   6:38 /usr/bin/python2 /usr/bin/nova-api
nova     11541  0.1  2.8 499372 168980 ?       S    Sep03   6:01 /usr/bin/python2 /usr/bin/nova-api
nova     11542  0.0  2.1 459788 125672 ?       S    Sep03   0:00 /usr/bin/python2 /usr/bin/nova-api
nova     11543  0.0  2.1 459888 125644 ?       S    Sep03   0:00 /usr/bin/python2 /usr/bin/nova-api

```


## 2. Telemetry Service¶


- Link tìm hiểu : ./ceilometer.md 

## 3. OpenStack Specific Resources

- Các tài nguyên ví dun như RAM, CPU, disk là các loại tài nguyên phổ thông mà các servver ảo hóa có và cũng là tài nguyên quan trọng của một máy ảo trên đó. Có thể theo dõi một số tài nguyên để tracking hệ thống 
```
openstack usage list
```

- Xem danh sách hypervisor
```
nova hypervisor-list
+--------------------------------------+---------------------+-------+---------+
| ID                                   | Hypervisor hostname | State | Status  |
+--------------------------------------+---------------------+-------+---------+
| 86d0610a-6eb4-49fd-86e4-53a718b5ce03 | compute1            | up    | enabled |
+--------------------------------------+---------------------+-------+---------+
```

- Xem info hypervisor
```
nova hypervisor-show 86d0610a-6eb4-49fd-86e4-53a718b5ce03
+---------------------------+------------------------------------------+
| Property                  | Value                                    |
+---------------------------+------------------------------------------+
| cpu_info_arch             | x86_64                                   |
| cpu_info_features         | ["pge", "avx", "clflush", "sep",         |
|                           | "syscall", "tsc_adjust", "tsc-deadline", |
|                           | "msr", "xsave", "vmx", "cmov", "fpu",    |
|                           | "pat", "arat", "lm", "tsc", "nx",        |
|                           | "fxsr", "sse4.1", "pae", "sse4.2",       |
|                           | "pclmuldq", "pcid", "vme", "mmx",        |
|                           | "osxsave", "cx8", "mce", "de", "aes",    |
|                           | "mca", "pse", "lahf_lm", "popcnt",       |
|                           | "apic", "sse", "ds", "invtsc", "pni",    |
|                           | "rdtscp", "sse2", "ss", "hypervisor",    |
|                           | "ssse3", "cx16", "pse36", "mtrr",        |
|                           | "x2apic"]                                |
| cpu_info_model            | SandyBridge                              |
| cpu_info_topology_cells   | 1                                        |
| cpu_info_topology_cores   | 1                                        |
| cpu_info_topology_sockets | 2                                        |
| cpu_info_topology_threads | 1                                        |
| cpu_info_vendor           | Intel                                    |
| current_workload          | 0                                        |
| disk_available_least      | 86                                       |
| free_disk_gb              | 83                                       |
| free_ram_mb               | 3487                                     |
| host_ip                   | 192.168.50.132                           |
| hypervisor_hostname       | compute1                                 |
| hypervisor_type           | QEMU                                     |
| hypervisor_version        | 2012000                                  |
| id                        | 86d0610a-6eb4-49fd-86e4-53a718b5ce03     |
| local_gb                  | 99                                       |
| local_gb_used             | 16                                       |
| memory_mb                 | 7999                                     |
| memory_mb_used            | 4512                                     |
| running_vms               | 1                                        |
| service_disabled_reason   | None                                     |
| service_host              | compute1                                 |
| service_id                | 99177238-b44d-4cd3-ab5b-04bd85e62ac3     |
| state                     | up                                       |
| status                    | enabled                                  |
| vcpus                     | 2                                        |
| vcpus_used                | 1                                        |
+---------------------------+------------------------------------------+

```

- Liệt kê VM trên hypervisor
```
nova hypervisor-servers compute1
+--------------------------------------+-------------------+--------------------------------------+---------------------+
| ID                                   | Name              | Hypervisor ID                        | Hypervisor Hostname |
+--------------------------------------+-------------------+--------------------------------------+---------------------+
| d514933a-ca6e-4a8b-8369-1f780ca7b37b | instance-00000008 | 86d0610a-6eb4-49fd-86e4-53a718b5ce03 | compute1            |
+--------------------------------------+-------------------+--------------------------------------+---------------------+
```

- Xem hypervisor statistic trên hoàn hệ thống 
```
nova hypervisor-stats
+----------------------+-------+
| Property             | Value |
+----------------------+-------+
| count                | 1     |
| current_workload     | 0     |
| disk_available_least | 86    |
| free_disk_gb         | 83    |
| free_ram_mb          | 3487  |
| local_gb             | 99    |
| local_gb_used        | 16    |
| memory_mb            | 7999  |
| memory_mb_used       | 4512  |
| running_vms          | 1     |
| vcpus                | 2     |
| vcpus_used           | 1     |
+----------------------+-------+
```


- VM stats
```
nova diagnostics win2012```

-  