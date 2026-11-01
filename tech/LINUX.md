# UBUNTU / LINUX – FULL CURRICULUM
## Linux System Administration & Engineering Mastery

**Chương trình:** Backend & Infrastructure Engineering Mastery  
**Cấp độ:** Foundation → Intermediate → Advanced → Expert  
**Thời lượng:** 10 tuần – 150 giờ  
**Cường độ:** 15 giờ/tuần  
**Hệ điều hành thực hành:** Ubuntu Server 24.04 LTS  
**Định hướng:** Backend Engineering, Linux System Administration, DevOps, Infrastructure Engineering.

---

# PHẦN I. MỤC TIÊU ĐÀO TẠO

## 1. Mục tiêu tổng quát

Sau khi hoàn thành chương trình, học viên có khả năng:

1. Hiểu kiến trúc Linux Operating System và Linux Kernel.
2. Sử dụng Linux CLI thành thạo.
3. Quản lý Filesystem, Disk, Partition và Storage.
4. Hiểu và quản lý Process, Thread, Signal.
5. Hiểu CPU Scheduling, Memory Management và I/O.
6. Quản lý Systemd, Service và Boot Process.
7. Cấu hình và phân tích Linux Networking.
8. Quản lý Package, Software và Dependency.
9. Viết Bash Script để tự động hóa công việc hệ thống.
10. Quản trị User, Group, Permission và Access Control.
11. Bảo mật Ubuntu Server theo hướng Production.
12. Phân tích System Logs và thực hiện Troubleshooting.
13. Monitoring, Performance Tuning và Resource Management.
14. Backup, Recovery và Disaster Recovery.
15. Triển khai và vận hành các ứng dụng Backend trên Ubuntu Server.

## 2. Chuẩn năng lực đầu ra

| Level | Năng lực |
|---|---|
| Foundation | Hiểu khái niệm và sử dụng được Linux CLI |
| Intermediate | Tự cài đặt, cấu hình và vận hành Ubuntu Server |
| Advanced | Debug, Troubleshoot, Security Hardening và Performance Tuning |
| Expert | Hiểu internals, thiết kế hệ thống, xử lý sự cố phức tạp và đưa ra quyết định kiến trúc |

Lưu ý: Expert không đồng nghĩa với việc thuộc tất cả câu lệnh Linux. Expert phải hiểu cơ chế, biết giới hạn của hệ thống, biết đo lường và có thể giải thích tại sao một giải pháp đúng trong một tình huống cụ thể.

---

# PHẦN II. KIẾN TRÚC CHƯƠNG TRÌNH

Chương trình gồm 15 module kiến thức.

| Module | Nội dung | Thời lượng dự kiến |
|---|---|---:|
| M01 | Linux Fundamentals & Architecture | 10 giờ |
| M02 | Linux Command Line & Shell Engineering | 10 giờ |
| M03 | Filesystem & Storage Management | 12 giờ |
| M04 | User, Group & Permission | 8 giờ |
| M05 | Process & Thread Management | 12 giờ |
| M06 | Systemd & Boot Process | 10 giờ |
| M07 | CPU, Memory & Resource Management | 12 giờ |
| M08 | Linux Networking | 12 giờ |
| M09 | Package Management & Software Administration | 8 giờ |
| M10 | Bash Scripting & Automation | 12 giờ |
| M11 | Linux Security & Hardening | 12 giờ |
| M12 | Logging, Monitoring & Observability | 8 giờ |
| M13 | Performance Analysis & Troubleshooting | 10 giờ |
| M14 | Backup, Recovery & Reliability | 6 giờ |
| M15 | Production Lab & Capstone Project | 8 giờ |
| **Tổng** | | **150 giờ** |

Các module được phân bổ theo tuần bên dưới. Một số kiến thức sẽ được học đan xen để bảo đảm có đủ thời gian thực hành và tích hợp.

---

# PHẦN III. CHI TIẾT GIÁO TRÌNH

# MODULE 01 – LINUX FUNDAMENTALS & ARCHITECTURE

**Thời lượng: 10 giờ**

## 1.1. Lịch sử và hệ sinh thái Linux

Kiến thức cần nắm:

- Unix là gì?
- Linux ra đời như thế nào?
- Linux Kernel là gì?
- Linux Distribution là gì?
- GNU và Linux có mối quan hệ như thế nào?
- Ubuntu là gì?
- Ubuntu Server và Ubuntu Desktop khác nhau như thế nào?
- LTS Release là gì?
- Linux Open Source Model.
- Linux Filesystem Hierarchy Standard.

Phân biệt các thành phần:

- Linux Kernel.
- GNU Utilities.
- Shell.
- System Libraries.
- User Applications.
- Package Manager.
- Init System.

## 1.2. Linux Architecture

Hiểu kiến trúc tổng thể:

```text
+----------------------------------+
|        User Applications         |
+----------------------------------+
|        System Libraries          |
+----------------------------------+
|        System Call Interface     |
+----------------------------------+
|          Linux Kernel            |
|                                  |
|  Process Management              |
|  Memory Management               |
|  Filesystem                      |
|  Networking                      |
|  Device Drivers                  |
+----------------------------------+
|            Hardware              |
|                                  |
| CPU | RAM | Disk | Network       |
+----------------------------------+
```

Các khái niệm:

- User Space.
- Kernel Space.
- System Calls.
- Kernel Mode.
- User Mode.
- Kernel Modules.
- Device Drivers.
- Hardware Abstraction.
- Monolithic Kernel và Modular Kernel.

## 1.3. Linux Kernel

Phải hiểu:

- Vai trò của Kernel.
- Kernel Version.
- Kernel Compilation ở mức khái niệm.
- Kernel Modules.
- Load và Unload Modules.
- Kernel Parameters.
- `/proc`.
- `/sys`.
- `/dev`.

Các lệnh:

```bash
uname -a
uname -r
hostnamectl
lsmod
modinfo
modprobe
dmesg
cat /proc/version
```

## 1.4. Linux System Information

Thực hành:

```bash
hostnamectl
lscpu
lsmem
free -h
lsblk
blkid
lspci
lsusb
uptime
```

Mục tiêu là đọc được thông tin phần cứng và tài nguyên của một Linux Server.

## 1.5. Kiểm tra kiến thức

Bạn phải giải thích được:

1. Linux Kernel khác Ubuntu Distribution như thế nào?
2. System Call có vai trò gì?
3. User Space và Kernel Space khác nhau ra sao?
4. Khi chạy một command trong terminal, chuyện gì xảy ra?
5. `/proc` và `/sys` khác nhau thế nào?
6. Linux Kernel có phải là một Process không?
7. Tại sao một chương trình User Space không thể tùy ý truy cập phần cứng?

## Lab M01

- Cài đặt Ubuntu Server.
- Kiểm tra Kernel Version.
- Kiểm tra CPU, RAM, Disk.
- Kiểm tra Kernel Modules.
- Khám phá `/proc`, `/sys`, `/dev`.
- Viết báo cáo kiến trúc máy chủ.

Deliverable:

`linux-architecture-report.md`

---

# MODULE 02 – LINUX COMMAND LINE & SHELL ENGINEERING

**Thời lượng: 10 giờ**

## 2.1. Shell Fundamentals

Kiến thức:

- Terminal là gì?
- Shell là gì?
- Bash là gì?
- Shell khác Terminal như thế nào?
- Interactive Shell.
- Login Shell.
- Non-interactive Shell.
- Environment Variables.
- PATH.
- Shell Configuration.

Các file cần hiểu:

```text
/etc/profile
/etc/bash.bashrc
~/.profile
~/.bashrc
~/.bash_logout
```

## 2.2. File and Directory Commands

```bash
pwd
ls
cd
mkdir
rmdir
touch
cp
mv
rm
file
stat
tree
find
locate
```

Phải hiểu:

- Absolute Path.
- Relative Path.
- Hidden Files.
- Wildcards.
- File Metadata.
- Directory Structure.

## 2.3. Text Processing

```bash
cat
less
more
head
tail
grep
sed
awk
cut
sort
uniq
wc
tr
tee
xargs
```

Phải thành thạo:

- Standard Input.
- Standard Output.
- Standard Error.
- Pipe.
- Redirection.
- Command Substitution.
- Exit Code.

Ví dụ:

```bash
grep "ERROR" application.log \
  | awk '{print $1, $2, $NF}' \
  | sort \
  | uniq -c \
  | sort -nr
```

Giải thích được từng bước dữ liệu đi qua Pipeline như thế nào.

## 2.4. Command Execution

Các kiến thức:

- PATH Resolution.
- Built-in Commands.
- External Commands.
- Alias.
- Function.
- Environment Variable.
- Exit Status.
- Command Chaining.

Ví dụ:

```bash
command_a && command_b
command_a || command_b
command_a ; command_b
```

## 2.5. Process trong Shell

```bash
command &
jobs
fg
bg
nohup
disown
wait
```

## Lab M02

1. Tìm toàn bộ file `.log` trong `/var/log`.
2. Tìm các dòng chứa `error`.
3. Đếm số lỗi theo từng loại.
4. Lọc 100 dòng log mới nhất.
5. Tổng hợp trạng thái các file log.
6. Viết một script kiểm tra thông tin hệ thống.

Deliverable:

`linux-cli-lab.md`

---

# MODULE 03 – FILESYSTEM & STORAGE MANAGEMENT

**Thời lượng: 12 giờ**

Đây là module quan trọng với người quản lý Linux Server.

## 3.1. Linux Filesystem Hierarchy

Phải hiểu ý nghĩa của:

```text
/
├── bin
├── boot
├── dev
├── etc
├── home
├── lib
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── sbin
├── srv
├── sys
├── tmp
├── usr
└── var
```

Các thư mục cần nghiên cứu sâu:

| Directory | Vai trò |
|---|---|
| `/etc` | System Configuration |
| `/var/log` | Log Files |
| `/var/lib` | Application State |
| `/var/cache` | Cache Data |
| `/var/tmp` | Temporary Files |
| `/home` | User Home Directories |
| `/root` | Root Home Directory |
| `/opt` | Optional Software |
| `/usr` | Userland Applications và Libraries |
| `/boot` | Boot-related Files |

## 3.2. Filesystem Concepts

- File.
- Directory.
- Inode.
- File Descriptor.
- Hard Link.
- Symbolic Link.
- Mount Point.
- Filesystem Metadata.
- File Permissions.
- Filesystem Types.

Các filesystem:

- ext4.
- XFS.
- Btrfs.
- tmpfs.
- OverlayFS.

Không chỉ cần biết tên mà phải hiểu đặc tính, ưu điểm và trường hợp sử dụng.

## 3.3. Disk Management

Các lệnh:

```bash
lsblk
blkid
fdisk
parted
partprobe
mkfs
mount
umount
findmnt
df
du
```

Kiến thức:

- Physical Disk.
- Partition Table.
- MBR.
- GPT.
- Partition.
- Filesystem.
- Mount.
- Swap Partition.
- Persistent Mount bằng `/etc/fstab`.

## 3.4. LVM

Phải hiểu:

- Physical Volume (PV).
- Volume Group (VG).
- Logical Volume (LV).
- Extend Volume.
- Reduce Volume.
- Filesystem Resize.
- Snapshot.

Thực hành trong VM riêng.

## 3.5. Disk I/O

Kiến thức:

- IOPS.
- Throughput.
- Latency.
- Sequential I/O.
- Random I/O.
- Read/Write.
- Page Cache.
- Disk Bottleneck.

Các công cụ:

```bash
iostat
iotop
lsblk
df
du
vmstat
```

## 3.6. Linux File Descriptor

Phải hiểu:

- File Descriptor là gì?
- Standard Input: FD 0.
- Standard Output: FD 1.
- Standard Error: FD 2.
- Open Files.
- File Descriptor Limit.
- `ulimit`.
- `/proc/<pid>/fd`.

## Lab M03

1. Tạo hai virtual disks trên VM.
2. Tạo Partition.
3. Format ext4.
4. Mount filesystem.
5. Cấu hình tự động mount qua `/etc/fstab`.
6. Thực hành Hard Link và Symbolic Link.
7. Kiểm tra inode.
8. Theo dõi disk usage.
9. Tìm file chiếm nhiều dung lượng.
10. Thử LVM snapshot và resize trên VM.

Câu hỏi kiểm tra:

- Tại sao `df` và `du` có thể cho kết quả khác nhau?
- Inode là gì?
- Tại sao xóa file nhưng disk space chưa được giải phóng?
- Hard Link khác Symbolic Link thế nào?
- Mount là gì?
- Nếu cấu hình sai `/etc/fstab`, điều gì có thể xảy ra khi boot?

Deliverable:

`filesystem-storage-lab.md`

---

# MODULE 04 – USER, GROUP & PERMISSION

**Thời lượng: 8 giờ**

## 4.1. User Management

- Root User.
- System User.
- Regular User.
- UID.
- GID.
- Primary Group.
- Supplementary Group.
- `/etc/passwd`.
- `/etc/shadow`.
- `/etc/group`.
- `/etc/gshadow`.

Các lệnh:

```bash
useradd
usermod
userdel
passwd
groupadd
groupmod
groupdel
id
groups
who
whoami
```

## 4.2. Linux Permission Model

Phải nắm:

- Read.
- Write.
- Execute.
- Owner.
- Group.
- Others.
- Numeric Permissions.
- Symbolic Permissions.

Ví dụ:

```bash
chmod 755 file
chmod 644 file
chmod 700 file
chown user:group file
chgrp group file
```

## 4.3. Advanced Permissions

- SUID.
- SGID.
- Sticky Bit.
- ACL.
- Default ACL.
- Umask.
- Capability.

Các lệnh:

```bash
getfacl
setfacl
getcap
setcap
umask
```

## 4.4. Sudo

- `/etc/sudoers`.
- `/etc/sudoers.d/`.
- Least Privilege.
- Privilege Escalation.
- Sudoers Syntax.
- Audit sudo activity.

## Lab M04

Thiết kế môi trường có các user:

- `developer`.
- `deploy`.
- `webapp`.
- `monitor`.

Yêu cầu:

1. Developer không có quyền root trực tiếp.
2. Deploy có quyền triển khai ứng dụng.
3. Webapp chỉ được đọc và ghi những thư mục cần thiết.
4. Monitor có quyền đọc các thông tin giám sát được cho phép.
5. Các nhóm không được truy cập trái phép vào dữ liệu của nhau.

Deliverable:

`user-permission-design.md`

---

# MODULE 05 – PROCESS & THREAD MANAGEMENT

**Thời lượng: 12 giờ**

Đây là module phải học sâu vì liên quan trực tiếp đến PHP-FPM, MySQL, Redis và Docker.

## 5.1. Process Fundamentals

- Process là gì?
- PID.
- PPID.
- Process Tree.
- Parent Process.
- Child Process.
- Process State.
- Foreground Process.
- Background Process.
- Daemon Process.

Các trạng thái:

- Running.
- Sleeping.
- Uninterruptible Sleep.
- Stopped.
- Zombie.

## 5.2. Process Creation

Phải hiểu:

- `fork()`.
- `exec()`.
- `wait()`.
- `exit()`.
- Copy-on-Write.

Mô tả được quá trình một Process tạo Process con và chuyển chương trình thực thi.

## 5.3. Thread

- Process vs Thread.
- Multithreading.
- User Threads.
- Kernel Threads.
- Shared Memory.
- Thread Synchronization.
- Context Switching.

## 5.4. Signal

Các Signal:

| Signal | Ý nghĩa |
|---|---|
| SIGTERM | Yêu cầu process kết thúc |
| SIGKILL | Buộc process kết thúc |
| SIGINT | Ngắt từ terminal |
| SIGHUP | Hangup, thường dùng để báo reload |
| SIGCHLD | Thông báo về child process |
| SIGSTOP | Dừng process |
| SIGCONT | Tiếp tục process |

Các lệnh:

```bash
ps
top
htop
pgrep
pkill
kill
killall
pstree
nice
renice
```

## 5.5. Process Management trong Production

Phải phân tích:

- Process bị treo.
- Zombie Process.
- Orphan Process.
- Process rò rỉ tài nguyên.
- Process ngốn CPU.
- Process chiếm nhiều RAM.
- File Descriptor Leak.
- Process Limit.

## 5.6. PHP-FPM Process Analysis

Thực hành trên môi trường PHP-FPM:

1. Xác định Master Process.
2. Xác định Worker Processes.
3. Quan sát Process Tree.
4. Đo mức RAM của Worker.
5. Kiểm tra số lượng Worker.
6. Theo dõi Worker khi tải tăng.
7. Phân tích Worker bị treo.
8. Tìm hiểu graceful reload và restart.

## Lab M05

- Viết một chương trình tạo nhiều child processes.
- Dùng `ps` để phân tích cây process.
- Gửi SIGTERM và SIGKILL.
- Tạo và quan sát một Zombie Process trong VM.
- Theo dõi CPU/RAM từng process.
- Phân tích PHP-FPM workers.

Deliverable:

`process-management-lab.md`

---

# MODULE 06 – SYSTEMD & BOOT PROCESS

**Thời lượng: 10 giờ**

## 6.1. Linux Boot Process

Phải hiểu:

```text
BIOS / UEFI
     |
     v
Bootloader (GRUB)
     |
     v
Linux Kernel
     |
     v
Init System (systemd)
     |
     v
System Services
     |
     v
Login / Target
```

Các khái niệm:

- BIOS.
- UEFI.
- GRUB.
- Bootloader.
- Kernel Initialization.
- Init System.
- PID 1.
- Runlevel.
- Systemd Target.

## 6.2. Systemd Architecture

Phải hiểu:

- Systemd.
- Units.
- Services.
- Targets.
- Sockets.
- Timers.
- Mount Units.
- Dependency Management.
- Startup Ordering.

## 6.3. Systemctl

```bash
systemctl status nginx
systemctl start nginx
systemctl stop nginx
systemctl restart nginx
systemctl reload nginx
systemctl enable nginx
systemctl disable nginx
systemctl list-units
systemctl list-unit-files
```

Phân biệt:

- Start vs Enable.
- Restart vs Reload.
- Active vs Enabled.
- Service Failure vs Service Disabled.

## 6.4. Custom Systemd Service

Tự tạo file:

```ini
[Unit]
Description=My Backend Application
After=network.target

[Service]
Type=simple
User=webapp
WorkingDirectory=/opt/myapp
ExecStart=/usr/bin/php /opt/myapp/worker.php
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Nghiên cứu thêm:

- `Type`.
- `ExecStart`.
- `ExecStartPre`.
- `ExecStop`.
- `Restart`.
- `RestartSec`.
- `User`.
- `Group`.
- `WorkingDirectory`.
- `Environment`.
- `EnvironmentFile`.
- `LimitNOFILE`.
- `TimeoutStartSec`.
- `KillMode`.

## 6.5. Systemd Timers

- Timer Units.
- Calendar Events.
- Monotonic Timers.
- Timer vs Cron.

## Lab M06

1. Viết một systemd service.
2. Tự động khởi chạy một PHP Worker.
3. Thiết lập Restart Policy.
4. Kiểm tra log.
5. Tạo systemd timer để chạy tác vụ backup.
6. Mô phỏng service crash và kiểm tra tự khởi động.

Deliverable:

`systemd-service-lab.md`

---

# MODULE 07 – CPU, MEMORY & RESOURCE MANAGEMENT

**Thời lượng: 12 giờ**

## 7.1. CPU Architecture

- CPU Core.
- Logical CPU.
- Hyper-Threading / SMT.
- CPU Scheduling.
- Context Switching.
- CPU Load.
- CPU Utilization.
- CPU Affinity.
- Run Queue.

Các lệnh:

```bash
lscpu
top
htop
mpstat
pidstat
vmstat
uptime
```

Phải phân biệt:

- CPU Usage.
- Load Average.
- I/O Wait.
- User Time.
- System Time.
- Idle Time.
- Steal Time.

## 7.2. Memory Management

- Physical Memory.
- Virtual Memory.
- Address Space.
- Memory Page.
- Page Table.
- Page Cache.
- Buffer Cache.
- Swap.
- Memory Mapping.
- Copy-on-Write.

Các lệnh:

```bash
free -h
vmstat
pmap
smem
cat /proc/meminfo
cat /proc/<PID>/status
```

## 7.3. Swap Management

- Swap Partition.
- Swap File.
- Swappiness.
- Memory Pressure.
- Swap In/Out.

Các lệnh:

```bash
swapon --show
swapoff
swapon
sysctl vm.swappiness
```

## 7.4. OOM Killer

Phải hiểu:

- Out Of Memory.
- Memory Pressure.
- OOM Killer.
- OOM Score.
- Memory Limits.
- Process Termination.

Thực hành phân tích OOM từ Kernel Logs.

## 7.5. Cgroups

Đây là kiến thức quan trọng khi sử dụng Docker.

Phải hiểu:

- Control Groups.
- CPU Controller.
- Memory Controller.
- I/O Controller.
- Resource Limits.
- Cgroups v1 vs v2.

Giải thích được Docker giới hạn CPU và RAM thông qua cơ chế nào.

## 7.6. Resource Limits

- `ulimit`.
- `/etc/security/limits.conf`.
- `systemd` resource controls.
- `LimitNOFILE`.
- `TasksMax`.
- `MemoryMax`.
- `CPUQuota`.

## Lab M07

1. Đo CPU Usage.
2. Quan sát Load Average.
3. Tạo chương trình tiêu thụ RAM trong VM.
4. Theo dõi Memory Pressure.
5. Mô phỏng OOM trong môi trường an toàn.
6. Kiểm tra Swap.
7. Phân tích cgroup.
8. Giới hạn tài nguyên của một process thông qua systemd.

Deliverable:

`cpu-memory-analysis.md`

---

# MODULE 08 – LINUX NETWORKING

**Thời lượng: 12 giờ**

Đây là nền tảng trước khi học chuyên sâu Network Engineering.

## 8.1. Network Interface

- NIC.
- Physical Interface.
- Virtual Interface.
- Loopback.
- MAC Address.
- MTU.
- Interface State.

Các lệnh:

```bash
ip addr
ip link
ip link show
ethtool
```

## 8.2. IP Addressing

- IPv4.
- IPv6.
- Netmask.
- CIDR.
- Private IP.
- Public IP.
- Loopback Address.
- Link-local Address.

## 8.3. Routing

- Routing Table.
- Default Gateway.
- Static Route.
- Kernel Routing.
- Policy Routing.

Các lệnh:

```bash
ip route
ip rule
ip route get
```

## 8.4. DNS

- DNS Resolver.
- `/etc/resolv.conf`.
- `/etc/hosts`.
- `/etc/nsswitch.conf`.
- systemd-resolved.
- DNS Caching.

Các lệnh:

```bash
resolvectl status
getent hosts example.com
dig example.com
nslookup example.com
```

## 8.5. TCP/UDP và Socket

- TCP Socket.
- UDP Socket.
- Listening Port.
- Established Connection.
- TIME_WAIT.
- CLOSE_WAIT.
- Connection Backlog.
- Socket Buffer.

Các lệnh:

```bash
ss -tulpn
ss -tan
lsof -i
nc
curl
```

## 8.6. Linux Firewall

- Netfilter.
- nftables.
- iptables.
- UFW.
- Firewall Rules.
- Input Chain.
- Output Chain.
- Forward Chain.

Không nhầm lẫn công cụ quản lý firewall với cơ chế xử lý packet bên dưới.

## 8.7. Packet Analysis

- TCP Handshake.
- Packet Capture.
- Network Interface.
- Packet Filtering.
- TCP Retransmission.
- MTU Issues.

Công cụ:

```bash
tcpdump
tshark
ip
ss
ethtool
```

## Lab M08

1. Kiểm tra Network Interfaces.
2. Xem Routing Table.
3. Kiểm tra DNS Resolver.
4. Kiểm tra TCP Connections.
5. Tạo một local TCP Server.
6. Dùng `tcpdump` quan sát kết nối.
7. Cấu hình UFW.
8. Phân tích lỗi không thể kết nối đến service.

Deliverable:

`linux-networking-lab.md`

---

# MODULE 09 – PACKAGE MANAGEMENT & SOFTWARE ADMINISTRATION

**Thời lượng: 8 giờ**

## 9.1. Package Management

- Package.
- Repository.
- Dependency.
- Package Metadata.
- Package Version.
- Package Signature.
- Software Source.

## 9.2. APT

Các lệnh:

```bash
apt update
apt upgrade
apt install
apt remove
apt purge
apt autoremove
apt show
apt list
apt-cache policy
apt-cache depends
```

Phải hiểu:

- APT.
- dpkg.
- Package Repository.
- GPG Signature.
- Dependency Resolution.
- Version Pinning.

## 9.3. System Software

- Install Software.
- Uninstall Software.
- Upgrade Software.
- Check Software Version.
- Manage Software Repository.
- Manage Third-party Repository.
- Package Conflict.

## 9.4. Software Deployment

Hiểu mối quan hệ:

```text
Source Code
    |
    v
Build / Package
    |
    v
Dependency Installation
    |
    v
Configuration
    |
    v
Systemd Service
    |
    v
Production Runtime
```

## Lab M09

1. Tạo danh sách package đang cài.
2. Kiểm tra dependency của một package.
3. Kiểm tra phiên bản package.
4. Cài đặt và gỡ bỏ một service.
5. Khôi phục cấu hình service sau khi nâng cấp.
6. Viết quy trình cập nhật phần mềm an toàn.

Deliverable:

`package-management-lab.md`

---

# MODULE 10 – BASH SCRIPTING & AUTOMATION

**Thời lượng: 12 giờ**

## 10.1. Bash Fundamentals

- Script Structure.
- Shebang.
- Variable.
- Environment Variable.
- Positional Parameters.
- Exit Code.
- Conditional.
- Loop.
- Function.
- Array.

## 10.2. Control Structures

```bash
if
case
for
while
until
```

## 10.3. Functions

- Function Definition.
- Arguments.
- Return Status.
- Local Variables.
- Scope.
- Reusable Functions.

## 10.4. Error Handling

- `set -e`.
- `set -u`.
- `set -o pipefail`.
- Trap.
- Exit Status.
- Logging.
- Error Output.

Không sử dụng các tùy chọn `set -euo pipefail` một cách máy móc. Phải hiểu tình huống mà từng tùy chọn có thể tạo ra hành vi ngoài dự kiến.

## 10.5. Input and Output

- Positional Arguments.
- Read Input.
- Standard Input.
- File Output.
- Here Document.
- Command Substitution.

## 10.6. Text Processing trong Automation

Kết hợp:

```bash
grep
awk
sed
cut
sort
uniq
find
xargs
```

## 10.7. Scheduling

- Cron.
- Crontab.
- `/etc/cron.d/`.
- Anacron.
- Systemd Timer.

## 10.8. Shell Script Engineering

Yêu cầu:

- Modular Functions.
- Input Validation.
- Error Handling.
- Logging.
- Exit Codes.
- Idempotency.
- Safe Execution.
- Documentation.

## Lab M10

Viết 5 Bash Scripts:

**Script 1: System Information**

Thu thập CPU, RAM, Disk, OS, Kernel.

**Script 2: Disk Monitoring**

Kiểm tra dung lượng disk và cảnh báo khi vượt ngưỡng.

**Script 3: Service Monitoring**

Kiểm tra trạng thái Nginx, PHP-FPM, MySQL, Redis.

**Script 4: Log Monitoring**

Theo dõi log và đếm các lỗi phổ biến.

**Script 5: Backup Automation**

Tự động backup thư mục ứng dụng và tạo log kết quả.

Deliverable:

```text
linux-automation/
├── system-info.sh
├── disk-monitor.sh
├── service-monitor.sh
├── log-monitor.sh
└── backup.sh
```

---

# MODULE 11 – LINUX SECURITY & HARDENING

**Thời lượng: 12 giờ**

## 11.1. Security Fundamentals

- CIA Triad.
- Least Privilege.
- Attack Surface.
- Defense in Depth.
- Authentication.
- Authorization.
- Auditing.
- Principle of Separation.

## 11.2. SSH Security

- SSH Protocol.
- Public Key Authentication.
- Private Key.
- Authorized Keys.
- SSH Agent.
- SSH Configuration.
- SSH Port.
- Password Authentication.
- Root Login.

Các file:

```text
/etc/ssh/sshd_config
~/.ssh/authorized_keys
~/.ssh/config
```

## 11.3. User Security

- Strong Password.
- Sudo Policy.
- Least Privilege.
- Account Locking.
- User Expiration.
- Session Management.

## 11.4. Permission Security

- Sensitive Files.
- Permission Audit.
- SUID/SGID Audit.
- World-writable Files.
- Default Umask.
- Linux Capabilities.

## 11.5. AppArmor

- Mandatory Access Control.
- AppArmor Profiles.
- Enforce Mode.
- Complain Mode.
- Profile Troubleshooting.

## 11.6. Firewall

- UFW.
- nftables.
- Allowlist.
- Denylist.
- Default Policies.
- Inbound Traffic.
- Outbound Traffic.

## 11.7. Security Updates

- Security Repository.
- Security Patches.
- Unattended Upgrades.
- Package Vulnerability.
- Kernel Updates.
- Reboot Management.

## 11.8. Audit

- Authentication Logs.
- Sudo Logs.
- System Logs.
- Auditd.
- File Integrity.
- Security Event Investigation.

## 11.9. Server Hardening

Thực hiện checklist:

1. Tắt các service không cần thiết.
2. SSH Key Authentication.
3. Hạn chế quyền Root Login qua SSH.
4. Thiết lập Least Privilege.
5. Cấu hình Firewall.
6. Kiểm soát Open Ports.
7. Cập nhật Security Patches.
8. Kiểm tra AppArmor.
9. Bảo vệ các file chứa Secret.
10. Kiểm tra quyền truy cập Log.
11. Cấu hình Time Synchronization.
12. Thiết lập Backup.
13. Kiểm tra các Security Events.

Lưu ý: Thay đổi SSH, firewall và security policy trên server production phải có phương án truy cập dự phòng và kiểm tra cấu hình trước khi áp dụng. Không khóa phiên quản trị duy nhất của mình.

## Lab M11

Tạo một Ubuntu Server có cấu hình ban đầu chưa harden.

Sau đó:

- Audit user và group.
- Audit SSH.
- Audit firewall.
- Audit service đang chạy.
- Audit file permissions.
- Kiểm tra AppArmor.
- Thiết lập security updates.
- Viết báo cáo trước và sau khi hardening.

Deliverable:

`ubuntu-security-hardening-report.md`

---

# MODULE 12 – LOGGING, MONITORING & OBSERVABILITY

**Thời lượng: 8 giờ**

## 12.1. Linux Logging Architecture

- Syslog.
- Journald.
- Rsyslog.
- Kernel Logs.
- Authentication Logs.
- Application Logs.
- Log Rotation.

Các file:

```text
/var/log/syslog
/var/log/auth.log
/var/log/kern.log
/var/log/dpkg.log
```

## 12.2. Journalctl

Các lệnh:

```bash
journalctl
journalctl -xe
journalctl -u nginx
journalctl -u php8.4-fpm
journalctl -f
journalctl --since today
journalctl -p err
```

## 12.3. Logrotate

- Rotation.
- Compression.
- Retention.
- Missing Log.
- Copytruncate.
- Postrotate.

## 12.4. Linux Monitoring

Các công cụ:

| Tool | Mục đích |
|---|---|
| top | CPU, Memory, Process |
| htop | Interactive Process Monitoring |
| vmstat | Memory và System Statistics |
| iostat | Disk I/O |
| mpstat | CPU Statistics |
| pidstat | Process Statistics |
| free | Memory |
| df | Disk Space |
| ss | Socket Statistics |
| sar | Historical System Statistics |

## 12.5. Metrics

Phải hiểu:

- CPU Usage.
- Memory Usage.
- Disk Utilization.
- Disk I/O Latency.
- Network Throughput.
- Packet Loss.
- Load Average.
- Process Count.
- File Descriptor Usage.

## Lab M12

Tạo một dashboard monitoring cơ bản cho Ubuntu Server.

Theo dõi:

- CPU.
- RAM.
- Disk.
- Network.
- Process.
- Service Availability.

Có thể nghiên cứu bổ sung Node Exporter và Prometheus ở phần mở rộng.

Deliverable:

`linux-monitoring-report.md`

---

# MODULE 13 – PERFORMANCE ANALYSIS & TROUBLESHOOTING

**Thời lượng: 10 giờ**

Đây là module chuyển từ Linux Administrator sang Linux/System Engineer.

## 13.1. Performance Analysis

Phải phân biệt:

- CPU Bottleneck.
- Memory Bottleneck.
- Disk I/O Bottleneck.
- Network Bottleneck.
- Process Bottleneck.
- Application Bottleneck.

## 13.2. Troubleshooting Methodology

Quy trình:

```text
Observe
   |
   v
Collect Evidence
   |
   v
Form Hypothesis
   |
   v
Run Diagnostics
   |
   v
Identify Root Cause
   |
   v
Apply Fix
   |
   v
Verify
   |
   v
Document
```

## 13.3. Advanced Linux Tools

Làm quen với:

- strace.
- ltrace.
- lsof.
- perf.
- sysstat.
- tcpdump.
- vmstat.
- iostat.
- pidstat.
- sar.
- dmesg.

Hiểu thêm về:

- `/proc`.
- `/sys`.
- Kernel Tracepoints.
- eBPF ở mức nhập môn và ứng dụng quan sát hệ thống.

## 13.4. Incident Scenarios

Phải tự xử lý ít nhất 10 tình huống:

1. CPU Usage đột ngột lên 100%.
2. RAM gần cạn.
3. Server bắt đầu sử dụng Swap liên tục.
4. Disk đầy.
5. Inode đầy.
6. Process không thể bị terminate thông thường.
7. Service liên tục Restart.
8. File Descriptor cạn.
9. Network Interface mất kết nối.
10. Kernel OOM Kill một ứng dụng.

## 13.5. Root Cause Analysis

Mỗi sự cố cần có:

- Incident Summary.
- Impact.
- Timeline.
- Evidence.
- Root Cause.
- Resolution.
- Prevention.
- Lessons Learned.

Deliverable:

`linux-incident-reports.md`

---

# MODULE 14 – BACKUP, RECOVERY & RELIABILITY

**Thời lượng: 6 giờ**

## 14.1. Backup Fundamentals

- Full Backup.
- Incremental Backup.
- Differential Backup.
- Snapshot.
- Off-site Backup.
- Backup Retention.

## 14.2. Recovery Concepts

- Recovery Time Objective (RTO).
- Recovery Point Objective (RPO).
- Disaster Recovery.
- Restore Testing.
- Recovery Procedure.

## 14.3. Linux Backup Tools

- tar.
- rsync.
- gzip.
- xz.
- cron.
- systemd timer.

Các lệnh:

```bash
tar
rsync
gzip
xz
```

## 14.4. Reliability

- Service Availability.
- Restart Strategy.
- Health Check.
- Redundancy.
- Monitoring.
- Failure Recovery.
- Graceful Shutdown.

## Lab M14

1. Backup application directory.
2. Backup Linux configuration.
3. Tạo lịch backup tự động.
4. Kiểm tra Backup Integrity.
5. Restore vào thư mục khác.
6. Xây dựng Recovery Procedure.
7. Ghi nhận RPO và RTO thực tế.

Deliverable:

`linux-backup-recovery-plan.md`

---

# MODULE 15 – PRODUCTION LAB & CAPSTONE PROJECT

**Thời lượng: 8 giờ**

## 15.1. Capstone Objective

Xây dựng một môi trường Ubuntu Server vận hành một ứng dụng Backend thực tế.

Kiến trúc:

```text
                    Internet
                        |
                        v
                  Ubuntu Server
                        |
                  Linux Firewall
                        |
                        v
                      Nginx
                        |
                        v
                    PHP-FPM
                        |
                        v
                    Laravel
                     /    \
                    /      \
                   v        v
                MySQL     Redis
```

Trong giai đoạn Linux, tập trung hiểu Ubuntu Host và quản lý các service. Docker sẽ được nghiên cứu sâu ở chủ đề riêng.

## 15.2. Yêu cầu triển khai

### A. Linux Administration

- Cài đặt Ubuntu Server.
- Thiết lập Hostname.
- Thiết lập Timezone.
- Cập nhật hệ thống.
- Tạo User và Group.
- Cấu hình SSH.

### B. Storage

- Phân tích Disk.
- Phân vùng và Mount.
- Theo dõi Disk Usage.
- Quản lý Log.

### C. Process và Services

- Quản lý Nginx.
- Quản lý PHP-FPM.
- Quản lý MySQL.
- Quản lý Redis.
- Phân tích Process Tree.

### D. Security

- SSH Hardening.
- User Permission.
- Firewall.
- Security Updates.
- AppArmor.

### E. Automation

- System Monitoring Script.
- Disk Monitoring Script.
- Service Monitoring Script.
- Backup Script.

### F. Observability

- Centralized System Logs ở mức cơ bản.
- Journalctl.
- CPU/RAM/Disk Monitoring.
- Service Health.

## 15.3. Failure Testing

Mô phỏng:

- Nginx Stop.
- PHP-FPM Stop.
- MySQL Stop.
- Redis Stop.
- Disk gần đầy.
- Process tiêu thụ RAM cao.
- Service không thể khởi động.
- SSH Authentication Failure.

Với mỗi sự cố, hãy:

1. Phát hiện.
2. Thu thập log.
3. Xác định nguyên nhân.
4. Khôi phục service.
5. Kiểm tra hoạt động.
6. Viết Incident Report.

## 15.4. Capstone Deliverables

```text
ubuntu-linux-mastery/
│
├── architecture/
│   ├── system-architecture.md
│   └── process-flow.md
│
├── configuration/
│   ├── ssh/
│   ├── systemd/
│   └── security/
│
├── scripts/
│   ├── system-info.sh
│   ├── disk-monitor.sh
│   ├── service-monitor.sh
│   └── backup.sh
│
├── reports/
│   ├── performance-report.md
│   ├── security-report.md
│   └── incident-report.md
│
├── backup/
│   └── recovery-plan.md
│
└── README.md
```

---

# PHẦN IV. KẾ HOẠCH HỌC TẬP 10 TUẦN

Mỗi tuần dành 15 giờ.

Phân bổ khuyến nghị:

- 3 giờ: Đọc lý thuyết và tài liệu.
- 3 giờ: Nghiên cứu kiến trúc và cơ chế bên trong.
- 6 giờ: Lab thực hành.
- 2 giờ: Troubleshooting.
- 1 giờ: Tổng kết và ghi chép.

## Week 1 – Linux Fundamentals & CLI

**Chủ đề:**
- Linux Architecture.
- Linux Kernel.
- User Space / Kernel Space.
- Shell Fundamentals.
- Linux CLI.

**Lab:**
- Ubuntu Installation.
- System Information.
- File Operations.
- Process Inspection.
- Text Processing.

**Đánh giá:**
Có thể giải thích được Linux Architecture và sử dụng CLI độc lập.

## Week 2 – Filesystem & Permission

**Chủ đề:**
- Linux Filesystem Hierarchy.
- Inode.
- File Descriptor.
- Hard Link / Symbolic Link.
- Mount.
- Disk Management.
- User / Group.
- Permission.

**Lab:**
- Partition.
- ext4.
- Mount.
- fstab.
- Permission.
- ACL.

**Đánh giá:**
Tự quản lý được Users, Permissions và Filesystem.

## Week 3 – Process Management

**Chủ đề:**
- Process.
- Thread.
- fork / exec.
- Signal.
- Process States.
- File Descriptors.
- Daemon.

**Lab:**
- Process Tree.
- Zombie Process.
- Signal.
- Process Monitoring.
- PHP-FPM Process Analysis.

**Đánh giá:**
Hiểu và phân tích được Process trong Linux.

## Week 4 – Systemd & Boot

**Chủ đề:**
- Boot Process.
- Kernel Initialization.
- systemd.
- Systemd Units.
- Service Management.
- Systemd Timer.

**Lab:**
- Custom Systemd Service.
- PHP Worker Service.
- Auto Restart.
- Timer.

**Đánh giá:**
Tự triển khai và vận hành được Linux Services.

## Week 5 – CPU, Memory & Resource

**Chủ đề:**
- CPU Scheduling.
- Load Average.
- Virtual Memory.
- Page Cache.
- Swap.
- OOM Killer.
- Cgroups.

**Lab:**
- CPU Load.
- Memory Pressure.
- OOM Simulation.
- Resource Limits.

**Đánh giá:**
Có khả năng xác định vấn đề CPU và Memory.

## Week 6 – Linux Networking

**Chủ đề:**
- Network Interface.
- IP Address.
- Routing.
- DNS.
- TCP/UDP.
- Socket.
- Firewall.
- Packet Capture.

**Lab:**
- DNS Debugging.
- TCP Connection.
- ss.
- tcpdump.
- UFW.

**Đánh giá:**
Có khả năng phân tích kết nối ở cấp độ Linux Host.

## Week 7 – Package Management & Automation

**Chủ đề:**
- APT.
- dpkg.
- Software Repositories.
- Bash Scripting.
- Cron.
- Systemd Timer.

**Lab:**
- System Information Script.
- Disk Monitoring.
- Service Monitoring.
- Backup Automation.

**Đánh giá:**
Tự động hóa được các công việc quản trị thông thường.

## Week 8 – Security Hardening

**Chủ đề:**
- Linux Security Model.
- SSH.
- Sudo.
- Permission Security.
- AppArmor.
- Firewall.
- Security Update.
- Audit.

**Lab:**
- SSH Hardening.
- Server Hardening.
- Security Audit.

**Đánh giá:**
Tạo được cấu hình Ubuntu Server theo nguyên tắc Least Privilege.

## Week 9 – Monitoring & Troubleshooting

**Chủ đề:**
- Journald.
- Syslog.
- Logrotate.
- System Monitoring.
- Performance Analysis.
- strace.
- lsof.
- perf.

**Lab:**
- CPU Incident.
- Memory Incident.
- Disk Incident.
- Service Incident.
- Root Cause Analysis.

**Đánh giá:**
Phân tích và giải quyết được sự cố Linux có bằng chứng.

## Week 10 – Production & Capstone

**Chủ đề:**
- Backup.
- Recovery.
- Reliability.
- Production Operations.
- Security Review.
- Performance Review.

**Lab:**
- Hoàn thiện môi trường Backend.
- Kiểm tra bảo mật.
- Mô phỏng sự cố.
- Restore.
- Viết tài liệu vận hành.

**Đánh giá:**
Hoàn thành Capstone và bảo vệ kiến trúc hệ thống.

---

# PHẦN V. MÔI TRƯỜNG THỰC HÀNH

## 1. Lab Environment

Đề xuất:

| Thành phần | Cấu hình |
|---|---|
| Host OS | Windows |
| Virtualization | Hyper-V hoặc VirtualBox |
| Guest OS | Ubuntu Server 24.04 LTS |
| CPU | 2–4 vCPU |
| RAM | 4–8 GB |
| Disk | 40–80 GB |
| Network | NAT + Host-only |
| Terminal | Windows Terminal / SSH |

Bạn đang có Ubuntu Server thực tế với cấu hình 4 CPU, RAM 31 GB và Docker. Hãy sử dụng máy ảo để thử nghiệm các tình huống rủi ro; server đang vận hành chỉ nên dùng để quan sát và thực hành các thao tác đã được kiểm chứng.

## 2. Required Tools

Các công cụ cần cài và sử dụng trong quá trình học:

```bash
sudo apt install \
  curl \
  wget \
  vim \
  nano \
  git \
  htop \
  iotop \
  sysstat \
  lsof \
  strace \
  tcpdump \
  net-tools \
  dnsutils \
  tree \
  jq \
  rsync
```

Không nhất thiết phải cài toàn bộ ngay ngày đầu tiên. Cài theo từng module và tìm hiểu lý do sử dụng.

## 3. Lab Rules

1. Không thử nghiệm destructive commands trên production.
2. Snapshot VM trước các Lab liên quan đến Disk, Boot và Firewall.
3. Ghi lại cấu hình trước khi thay đổi.
4. Đọc log trước khi khắc phục.
5. Không chạy lệnh không hiểu rõ.
6. Đo hiệu năng trước và sau khi tối ưu.
7. Mỗi Lab phải có kết quả và tài liệu.
8. Mọi thao tác bảo mật phải có phương án rollback.

---

# PHẦN VI. TÀI LIỆU HỌC TẬP

## 1. Official Documentation

Ưu tiên học từ tài liệu chính thức:

1. Ubuntu Server Guide:
   https://documentation.ubuntu.com/server/

2. Ubuntu Documentation:
   https://help.ubuntu.com/

3. Linux Kernel Documentation:
   https://docs.kernel.org/

4. Linux Manual Pages:
   https://man7.org/linux/man-pages/

5. systemd Documentation:
   https://www.freedesktop.org/software/systemd/man/

6. GNU Bash Manual:
   https://www.gnu.org/software/bash/manual/

7. Ubuntu Security:
   https://ubuntu.com/security

## 2. Sách chuyên ngành

**Level Foundation:**

- The Linux Command Line – William Shotts.
- Linux Basics for Hackers – OccupyTheWeb (chỉ dùng phần nền tảng Linux, không phải giáo trình quản trị production).

**Level Intermediate:**

- How Linux Works – Brian Ward.
- UNIX and Linux System Administration Handbook – Evi Nemeth và cộng sự.

**Level Advanced:**

- The Linux Programming Interface – Michael Kerrisk.
- Linux System Programming – Robert Love.
- Systems Performance – Brendan Gregg.

**Level Expert:**

- Linux Kernel Development – Robert Love.
- BPF Performance Tools – Brendan Gregg.
- Tìm hiểu Linux Kernel Documentation và mã nguồn Linux Kernel.

Lưu ý: Một số sách sử dụng phiên bản Linux hoặc Ubuntu cũ. Cần đối chiếu với tài liệu chính thức của Ubuntu hiện hành, đặc biệt đối với systemd, cgroups, networking và security.

## 3. Công cụ học tập

- Linux Journey: https://linuxjourney.com/
- OverTheWire Bandit: https://overthewire.org/wargames/bandit/
- SadServers: https://sadservers.com/
- ExplainShell: https://explainshell.com/

Dùng các nền tảng này để bổ sung thực hành, không thay thế việc tự xây dựng Lab.

---

# PHẦN VII. ĐÁNH GIÁ NĂNG LỰC

## 1. Thang điểm

| Tiêu chí | Trọng số |
|---|---:|
| Lý thuyết và kiến trúc | 15% |
| Command Line | 10% |
| System Administration | 15% |
| Process / Memory / CPU | 15% |
| Filesystem / Storage | 10% |
| Networking | 10% |
| Security | 10% |
| Troubleshooting | 10% |
| Automation | 5% |
| **Tổng** | **100%** |

## 2. Tiêu chí đánh giá

**Foundation**

- Đạt từ 60/100.
- Thực hiện được Linux CLI.
- Hiểu khái niệm cơ bản.

**Intermediate**

- Đạt từ 70/100.
- Hoàn thành các Lab quản trị.
- Tự cài đặt và cấu hình được service.

**Advanced**

- Đạt từ 80/100.
- Xử lý được các tình huống sự cố.
- Hiểu Resource Management.
- Có khả năng Security Hardening và Performance Analysis.

**Expert Readiness**

- Đạt từ 90/100.
- Hoàn thành Capstone.
- Giải thích được các cơ chế nội bộ.
- Đưa ra quyết định có cơ sở và phân tích Trade-off.
- Có thể bảo vệ phương án kỹ thuật trước các câu hỏi phản biện.

Điểm số không tự động chứng minh năng lực Expert. Cần xem xét kết quả Lab, tính chính xác của phân tích và khả năng xử lý những tình huống chưa từng gặp.

---

# PHẦN VIII. ĐỀ THI CUỐI KHÓA

## Part 1 – Linux Theory

40 câu hỏi về:

- Linux Architecture.
- Kernel.
- Process.
- Thread.
- Memory.
- Filesystem.
- Permission.
- Systemd.
- Networking.
- Security.

## Part 2 – Command Line Practical

Thực hiện 20 yêu cầu trên Ubuntu Server mà không dựa vào hướng dẫn từng bước.

## Part 3 – Troubleshooting

Giải quyết 5 sự cố ngẫu nhiên:

1. High CPU.
2. High Memory Usage.
3. Disk Full.
4. Service Failure.
5. Network Connectivity Failure.

## Part 4 – System Design

Thiết kế một Ubuntu Server phục vụ hệ thống Backend có:

- Nginx.
- PHP-FPM.
- Laravel.
- MySQL.
- Redis.

Yêu cầu giải thích:

- Process Architecture.
- Resource Allocation.
- Service Management.
- User Permissions.
- Security Policy.
- Monitoring Strategy.
- Backup Strategy.
- Failure Recovery.

## Part 5 – Technical Defense

Giảng viên đặt câu hỏi phản biện về các quyết định kỹ thuật.

Ví dụ:

- Tại sao chọn systemd thay vì tự dùng nohup?
- Tại sao service nên chạy bằng system user?
- Khi nào cần Swap?
- Tại sao Load Average cao nhưng CPU Usage thấp?
- Điều gì xảy ra khi OOM Killer hoạt động?
- Một process bị treo ở D state có thể xử lý như thế nào?
- Tại sao `df` báo đầy disk dù `du` không thấy file lớn?
- Tại sao một service active nhưng ứng dụng vẫn không truy cập được?

---

# PHẦN IX. DEFINITION OF DONE

Chỉ đánh dấu hoàn thành Ubuntu/Linux Full Curriculum khi đáp ứng tất cả điều kiện sau:

- [ ] Hiểu Linux Architecture.
- [ ] Thành thạo Linux CLI.
- [ ] Quản lý Filesystem và Storage.
- [ ] Quản lý User, Group và Permission.
- [ ] Hiểu Process và Thread.
- [ ] Phân tích được CPU và Memory.
- [ ] Quản lý Systemd và Boot Process.
- [ ] Cấu hình được Linux Networking.
- [ ] Quản lý Package và Software.
- [ ] Viết được Bash Scripts có xử lý lỗi.
- [ ] Hardening được Ubuntu Server.
- [ ] Phân tích được Linux Logs.
- [ ] Monitoring được tài nguyên.
- [ ] Troubleshoot được các sự cố phổ biến.
- [ ] Thực hiện được Backup và Recovery.
- [ ] Hoàn thành Production Capstone.
- [ ] Bảo vệ thành công Technical Defense.

---

# PHẦN X. NGUYÊN TẮC ĐÀO TẠO TRONG PROJECT CHATGPT

Khi hướng dẫn chương trình này, ChatGPT phải hoạt động như một Linux System Engineering Mentor.

## 1. Phương pháp giảng dạy

Mỗi bài học phải đi theo cấu trúc:

1. Learning Objectives.
2. Prerequisites.
3. Fundamental Concepts.
4. Architecture.
5. How It Works Internally.
6. Practical Examples.
7. Hands-on Lab.
8. Troubleshooting.
9. Advanced Knowledge.
10. Knowledge Assessment.

## 2. Quy tắc kiểm tra kiến thức

- Mỗi lần đặt một câu hỏi.
- Chờ học viên trả lời.
- Phân tích câu trả lời.
- Chỉ ra phần đúng và sai.
- Giải thích cơ chế kỹ thuật.
- Đưa ví dụ thực tế.
- Không tiết lộ đáp án trước khi học viên thử, trừ khi được yêu cầu.

## 3. Quy tắc thực hành

Với mỗi command hoặc configuration:

- Giải thích command.
- Giải thích từng tham số quan trọng.
- Nêu quyền cần thiết.
- Mô tả kết quả mong đợi.
- Nêu tác động lên hệ thống.
- Nêu rủi ro.
- Hướng dẫn xác minh kết quả.
- Cung cấp phương án rollback khi phù hợp.

Không đưa lệnh destructive nếu chưa giải thích rõ tác động.

## 4. Quy tắc sử dụng tài liệu upload

- Ưu tiên tài liệu người học upload.
- Chỉ rõ tên tài liệu, trang hoặc mục khi có thể xác định.
- Không tự suy diễn những nội dung không có trong tài liệu.
- Khi tài liệu lỗi thời, cần thông báo.
- Phân biệt kiến thức trong tài liệu với kiến thức bổ sung từ nguồn khác.
- Khi cần thông tin phiên bản hiện hành, đối chiếu tài liệu Ubuntu/Linux chính thức.

## 5. Theo dõi tiến độ

ChatGPT phải duy trì:

- Module đã hoàn thành.
- Bài học đã hoàn thành.
- Lab đã hoàn thành.
- Điểm kiểm tra.
- Kiến thức còn yếu.
- Những nội dung cần học lại.
- Năng lực hiện tại.
- Module tiếp theo.

Chỉ đánh dấu hoàn thành khi học viên chứng minh được năng lực qua câu hỏi và thực hành.

---

# KẾT QUẢ CUỐI CÙNG

Khi hoàn thành chương trình này, học viên phải có khả năng quản trị một Ubuntu Server ở mức Advanced, hiểu sâu các cơ chế hệ điều hành quan trọng và có khả năng phân tích sự cố ở cấp độ System Engineering.

Đây là nền tảng để tiếp tục học chuyên sâu:

1. Network Engineering.
2. Nginx & Reverse Proxy.
3. PHP Runtime & PHP-FPM.
4. MySQL Database Engineering.
5. Redis Engineering.
6. Docker & Container Internals.
7. Docker Compose & Production Deployment.
8. Backend System Architecture.

**Triết lý đào tạo:**

Không học Linux chỉ để biết câu lệnh.

Học Linux để hiểu hệ thống, kiểm soát tài nguyên, phân tích hành vi, tìm Root Cause, tối ưu và vận hành hạ tầng một cách có trách nhiệm.