# Roadmap dự án SysEng Lab

## Môi trường xuyên suốt

- Máy thật: Windows 10
- Ảo hóa: VMware Workstation
- Hệ điều hành chính: Ubuntu Server 24.04 LTS
- Quản trị từ Windows qua SSH
- Trình soạn thảo: Visual Studio Code
- Quản lý cấu hình và source code bằng Git

Kiến trúc mục tiêu:

```text
Windows 10
    |
    | VMware Workstation
    |
    +-- ubuntu-lb01
    |      Nginx
    |      Reverse proxy
    |      Load balancer
    |      Bastion
    |
    +-- ubuntu-app01
    |      Application
    |      Docker
    |      Laravel
    |      Worker
    |      Kubernetes / k3s
    |
    +-- ubuntu-data01
           MySQL
           PostgreSQL
           Redis
           Kafka
           Monitoring
```

Giai đoạn đầu chỉ cần một máy:

```text
ubuntu-node01
```

Cấu hình đề xuất:

```text
CPU:  2 vCPU
RAM:  4 GB
Disk: 50 GB

Adapter 1: NAT
Adapter 2: Host-only
```

---

# Giai đoạn 1 — Ubuntu Server Foundation

## Lab 01 — Tạo Ubuntu Server đầu tiên

Máy sử dụng:

```text
ubuntu-node01
```

Nội dung:

1. Tạo máy ảo trên VMware Workstation
2. Cài Ubuntu Server 24.04 LTS
3. Tạo user quản trị
4. Đặt hostname
5. Cập nhật hệ thống
6. Kiểm tra CPU, RAM và disk
7. Kiểm tra network interface
8. Cấu hình NAT và Host-only
9. Đặt static IP bằng Netplan
10. Cài OpenSSH Server
11. Kết nối SSH từ Windows
12. Tạo SSH key
13. Cấu hình timezone `Asia/Ho_Chi_Minh`
14. Cài VMware Tools
15. Tạo snapshot nền

Snapshot:

```text
00-clean-install
01-network-ready
02-ssh-ready
```

Kết quả cần đạt:

- Hiểu VM, NAT, Host-only
- Biết kiểm tra interface bằng `ip address`
- Hiểu default route
- Biết cấu hình Netplan
- SSH được từ Windows vào Ubuntu
- Biết kiểm tra service và log SSH

---

## Lab 02 — Linux command line cơ bản

Nội dung:

- Cấu trúc thư mục Linux
- Đường dẫn tuyệt đối và tương đối
- `ls`, `cd`, `pwd`
- `cp`, `mv`, `rm`, `mkdir`
- `cat`, `less`, `head`, `tail`
- `grep`, `find`
- Redirect và pipe
- Wildcard
- Đọc file trong `/etc`, `/var/log`, `/proc`

Bài thực hành:

- Tạo cấu trúc thư mục dự án
- Tìm kiếm file cấu hình
- Lọc log
- Gộp và xử lý file text

---

## Lab 03 — User, group và permission

Nội dung:

- User và group trên Ubuntu
- `/etc/passwd`, `/etc/group`, `/etc/shadow`
- `useradd`, `adduser`, `usermod`
- `chmod`, `chown`, `chgrp`
- Quyền `rwx`
- SUID, SGID, sticky bit
- `sudo` và nhóm `sudo`

Bài thực hành:

- Tạo user developer
- Tạo nhóm vận hành
- Phân quyền thư mục application
- Mô phỏng lỗi `Permission denied`

---

## Lab 04 — Process và systemd

Nội dung:

- Process và PID
- `ps`, `top`, `htop`
- `kill`, `pkill`
- Foreground và background
- `systemctl`
- Unit file
- Service tự khởi động
- `journalctl`

Bài thực hành:

- Tạo một custom systemd service
- Start, stop, restart service
- Cấu hình service tự chạy khi boot
- Troubleshoot service bị lỗi

---

# Giai đoạn 2 — Network và Remote Administration

## Lab 05 — Linux networking

Nội dung:

- IP address
- Subnet mask
- Gateway
- DNS
- Default route
- NAT, Host-only, Bridged
- TCP và UDP
- Port
- Interface và routing table

Công cụ:

```bash
ip address
ip route
ping
traceroute
ss
curl
dig
resolvectl
```

Bài thực hành:

- Kiểm tra đường đi từ Ubuntu ra Internet
- Phân biệt traffic NAT và Host-only
- Mô phỏng lỗi sai gateway
- Mô phỏng lỗi DNS

---

## Lab 06 — SSH nâng cao

Nội dung:

- SSH key authentication
- `authorized_keys`
- Windows `~/.ssh/config`
- Tắt root login
- Tắt password login sau khi key hoạt động
- SSH agent
- Copy file bằng `scp`
- Đồng bộ bằng `rsync`
- SSH tunnel cơ bản

Cấu hình Windows:

```text
Host ubuntu-node01
    HostName 192.168.56.21
    User sysadmin
```

---

## Lab 07 — Firewall trên Ubuntu

Snapshot trước lab:

```text
03-before-firewall-lab
```

Nội dung:

- UFW
- nftables
- Allow và deny port
- Chỉ cho phép SSH từ mạng Host-only
- Kiểm tra port đang listen
- Log firewall

Bài thực hành:

- Mở port 22
- Mở port 80 và 443
- Chặn một port thử nghiệm
- Mô phỏng trường hợp firewall làm mất SSH
- Rollback từ VMware console

---

# Giai đoạn 3 — Storage và hệ thống file

## Lab 08 — Disk, partition và filesystem

Nội dung:

- Disk và partition
- `/dev/sda`, `/dev/sdb`
- `lsblk`
- `fdisk`
- `parted`
- Filesystem ext4
- Mount và unmount
- `/etc/fstab`

Bài thực hành:

- Thêm virtual disk trong VMware
- Tạo partition
- Format ext4
- Mount vào `/data`
- Tự động mount sau reboot

---

## Lab 09 — LVM

Snapshot:

```text
04-before-lvm-lab
```

Nội dung:

- Physical Volume
- Volume Group
- Logical Volume
- Mở rộng filesystem
- Thu hồi và khôi phục dữ liệu lab

Bài thực hành:

- Tạo VG và LV
- Mount vào `/srv/app`
- Mở rộng logical volume
- Kiểm tra dung lượng trước và sau

---

## Lab 10 — Backup và restore

Nội dung:

- `tar`
- `gzip`
- `rsync`
- Backup cấu hình `/etc`
- Backup application
- Restore file
- Cron backup
- Phân biệt snapshot và backup

---

# Giai đoạn 4 — Web Server và Application

## Lab 11 — Cài Nginx

Nội dung:

- Cài package bằng `apt`
- Service Nginx
- Document root
- Server block
- Access log và error log
- Port 80
- Firewall rule

Bài thực hành:

- Tạo website tĩnh
- Truy cập từ Windows
- Tạo nhiều virtual host
- Mô phỏng lỗi cấu hình Nginx

---

## Lab 12 — Reverse proxy

Nội dung:

- Reverse proxy là gì
- Upstream application
- Header proxy
- Timeout
- Access log
- Health check cơ bản

Kiến trúc:

```text
Windows
   |
   v
Nginx :80
   |
   v
Application :8080
```

---

## Lab 13 — PHP và Laravel trên Ubuntu

Nội dung:

- PHP-FPM
- Composer
- Extension PHP
- Laravel `.env`
- Permission của `storage` và `bootstrap/cache`
- Nginx kết nối PHP-FPM
- systemd service cho queue worker

Bài thực hành:

- Deploy Laravel
- Kết nối database
- Chạy migration
- Tạo queue worker
- Troubleshoot lỗi permission

---

## Lab 14 — HTTPS với Certbot

Nội dung:

- TLS/SSL
- Certificate
- Certbot
- Auto renew
- Redirect HTTP sang HTTPS
- Kiểm tra certificate

Lab này cần domain thật hoặc DNS nội bộ phù hợp.

---

# Giai đoạn 5 — Database và Cache

Khi bắt đầu giai đoạn này, tạo thêm máy:

```text
ubuntu-data01
```

Cấu hình:

```text
CPU:  2–4 vCPU
RAM:  4 GB
Disk: 60 GB
IP:   192.168.56.31
```

## Lab 15 — MySQL Server

Nội dung:

- Cài MySQL
- Service MySQL
- User và privilege
- Bind address
- Cho phép kết nối từ application server
- Backup bằng `mysqldump`
- Slow query log

---

## Lab 16 — PostgreSQL

Nội dung:

- Cluster PostgreSQL
- Role và database
- `pg_hba.conf`
- `postgresql.conf`
- Remote connection
- Backup và restore
- Process và connection

---

## Lab 17 — Redis

Nội dung:

- Redis service
- Key và data type
- Persistence
- Memory
- Authentication
- Bind address
- Laravel cache và queue

---

# Giai đoạn 6 — Git và triển khai ứng dụng

## Lab 18 — Git trên Ubuntu

Nội dung:

- Repository
- Branch
- Commit
- Remote
- Pull và push
- `.gitignore`
- SSH key cho Git
- Quản lý configuration bằng Git

Bài thực hành:

- Tạo repository cấu hình lab
- Commit Nginx config
- Commit systemd service
- Rollback cấu hình bằng Git

---

## Lab 19 — Deployment workflow

Nội dung:

- Clone source
- Environment variables
- Build application
- Migration
- Cache config
- Restart service
- Rollback version

Luồng:

```text
Developer
   |
   v
Git repository
   |
   v
ubuntu-app01
   |
   v
Nginx + Laravel
```

---

# Giai đoạn 7 — Docker trên Ubuntu

## Lab 20 — Docker Engine

Máy sử dụng:

```text
ubuntu-app01
```

Nội dung:

- Cài Docker Engine trên Ubuntu
- Docker daemon
- Image
- Container
- Volume
- Network
- Port mapping
- Log container

Không dùng Docker Desktop làm môi trường chính.

---

## Lab 21 — Docker Compose

Nội dung:

- Compose file
- Multi-container application
- Environment file
- Volume
- Network
- Health check
- Restart policy

Project thực hành:

```text
Nginx
Laravel
MySQL hoặc PostgreSQL
Redis
Queue worker
```

---

## Lab 22 — Docker troubleshooting

Nội dung:

- Container không start
- Port conflict
- Permission volume
- DNS container
- Network connection
- Log
- Resource limits

---

# Giai đoạn 8 — Monitoring và Logging

Có thể tạo thêm:

```text
ubuntu-monitor01
```

## Lab 23 — Linux monitoring

Công cụ:

```bash
free
uptime
vmstat
iostat
df
du
ss
journalctl
```

Nội dung:

- CPU
- RAM
- Disk
- Load average
- Process
- Network
- Log

---

## Lab 24 — Prometheus và Node Exporter

Nội dung:

- Metric
- Scrape
- Target
- Node Exporter
- PromQL cơ bản
- Theo dõi CPU, RAM, disk và network

---

## Lab 25 — Grafana

Nội dung:

- Datasource
- Dashboard
- Panel
- Alert
- Dashboard cho Ubuntu nodes

---

## Lab 26 — Logging tập trung

Công nghệ:

```text
Loki
Promtail
Grafana
```

Nội dung:

- Thu thập log Nginx
- Thu thập systemd journal
- Tìm kiếm lỗi theo thời gian
- Phân tích lỗi application

---

# Giai đoạn 9 — Load Balancing và High Availability

Tạo thêm:

```text
ubuntu-lb01
ubuntu-app02
```

## Lab 27 — Nginx Load Balancer

Kiến trúc:

```text
ubuntu-lb01
    |
    +-- ubuntu-app01
    |
    +-- ubuntu-app02
```

Nội dung:

- Upstream
- Round robin
- Least connections
- Health check
- Failover
- Sticky session
- Log upstream

---

## Lab 28 — Database backup và replication

Nội dung:

- MySQL replication hoặc PostgreSQL streaming replication
- Primary và replica
- Replication lag
- Failover cơ bản
- Backup trước thay đổi

---

## Lab 29 — High Availability cơ bản

Nội dung:

- Single point of failure
- Virtual IP
- Keepalived
- Active-passive
- Health check
- Split-brain cơ bản

---

# Giai đoạn 10 — Kubernetes hoặc k3s

Snapshot trước khi bắt đầu:

```text
05-before-kubernetes-lab
```

Có thể tạo:

```text
ubuntu-k8s-master01
ubuntu-k8s-worker01
ubuntu-k8s-worker02
```

## Lab 30 — Kubernetes foundation

Nội dung:

- Control plane
- Worker node
- Pod
- Deployment
- Service
- Namespace
- ConfigMap
- Secret

---

## Lab 31 — Deploy application lên Kubernetes

Nội dung:

- Laravel deployment
- Nginx
- Worker
- Service
- ConfigMap
- Secret
- Persistent volume
- Health probes

---

## Lab 32 — Ingress

Nội dung:

- Ingress Controller
- Domain nội bộ
- `/etc/hosts` trên Windows
- TLS
- Routing theo host và path

---

## Lab 33 — Kubernetes troubleshooting

Công cụ:

```bash
kubectl get
kubectl describe
kubectl logs
kubectl exec
kubectl top
kubectl events
```

Lỗi thực hành:

- Pod CrashLoopBackOff
- ImagePullBackOff
- Pending pod
- Service không truy cập được
- DNS lỗi
- Volume lỗi

---

# Giai đoạn 11 — Kafka và hệ thống phân tán

## Lab 34 — Kafka cơ bản

Nội dung:

- Broker
- Topic
- Partition
- Producer
- Consumer
- Consumer group
- Offset
- Retention

---

## Lab 35 — Kafka cluster

Nội dung:

- Multi-broker
- Replication factor
- Leader
- ISR
- Broker failure
- Rebalance

---

## Lab 36 — Kafka Connect

Nội dung:

- Source connector
- Sink connector
- Task
- Offset
- Retry
- Dead letter queue
- Database source và sink

---

# Giai đoạn 12 — Automation và vận hành thực tế

## Lab 37 — Bash scripting

Nội dung:

- Variable
- Condition
- Loop
- Function
- Exit code
- Log
- Error handling

Bài thực hành:

- Health-check script
- Backup script
- Deployment script
- Disk alert script

---

## Lab 38 — Cron và systemd timer

Nội dung:

- Cron job
- systemd timer
- Scheduled backup
- Scheduled cleanup
- Log job

---

## Lab 39 — Ansible

Nội dung:

- Inventory
- SSH
- Ad-hoc command
- Playbook
- Role
- Template
- Handler

Bài thực hành:

- Cài Nginx đồng loạt
- Tạo user trên nhiều nodes
- Deploy configuration
- Restart service khi config thay đổi

---

## Lab 40 — CI/CD

Nội dung:

- Build
- Test
- Deploy
- Environment
- Secret
- Rollback
- Pipeline log

Có thể sử dụng:

```text
GitHub Actions
hoặc
Azure DevOps
```

---

# Project tổng hợp cuối roadmap

Kiến trúc cuối:

```text
Windows 10
    |
    | SSH / HTTPS
    v
ubuntu-lb01
    |
    | Nginx Load Balancer
    |
    +-- ubuntu-app01
    |      Laravel
    |      Docker
    |      Worker
    |
    +-- ubuntu-app02
           Laravel
           Docker
           Worker

ubuntu-data01
    |
    +-- MySQL / PostgreSQL
    +-- Redis
    +-- Kafka

ubuntu-monitor01
    |
    +-- Prometheus
    +-- Grafana
    +-- Loki
```

Các chức năng cần hoàn thành:

- Website hoạt động qua HTTPS
- Nginx reverse proxy và load balancing
- Hai application nodes
- Database riêng
- Redis cache và queue
- Monitoring CPU, RAM, disk và service
- Log tập trung
- Backup tự động
- Deploy bằng Git hoặc CI/CD
- Firewall giới hạn port
- Tài liệu troubleshooting và rollback

---

# Thứ tự ưu tiên học

```text
Ubuntu cơ bản
    ↓
Network và SSH
    ↓
Permission và systemd
    ↓
Storage và backup
    ↓
Nginx và Laravel
    ↓
MySQL / PostgreSQL / Redis
    ↓
Git và deployment
    ↓
Docker
    ↓
Monitoring
    ↓
Load balancing và HA
    ↓
Kubernetes
    ↓
Kafka
    ↓
Ansible và CI/CD
```

Hiện tại nên tiếp tục hoàn thành **Lab 01 trên `ubuntu-node01`**, đặc biệt là phần NAT, Host-only, static IP Netplan và SSH, trước khi chuyển sang Lab 02.
