#!/usr/bin/env python3
"""
🏴 LEARN WITH N4MR3S
COMPLETE WORKING VERSION - ALL 50 LEVELS
"""

import os
import sys
import time
import json
import random
import threading
import socket
import webbrowser
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from datetime import datetime

# ============================================
# COLOR CODES
# ============================================

class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'

# ============================================
# ALL 50 LEVELS - COMPLETE DICTIONARY
# ============================================

LEVELS = {
    1: {
        "name": "🌱 The Beginning",
        "description": "Your first step into the Linux world",
        "what_you_learn": "Basic navigation commands: ls, pwd, and understanding the file system",
        "objective": "Learn basic navigation and file listing",
        "category": "Beginner",
        "difficulty": 1,
        "hint": "Use 'ls' to list files, 'pwd' to show your location",
        "flag": "CTF{hello_linux_2024}",
        "tasks": [
            {"instruction": 'Use `ls` to see all files and folders in the directory you are currently in.', "check": "ls"},
            {"instruction": 'Use `pwd` to find the full path of the directory you are currently in.', "check": "pwd"},
            {"instruction": 'Use `ls -a` to display all files and folders, including hidden ones.', "check": "ls -a"},
            {"instruction": 'Use `ls -l` to display files with details such as permissions, owner, size, and modification time.', "check": "ls -l"}
        ]
    },
    2: {
        "name": "🧭 Navigation Master",
        "description": "Learn to move around the filesystem",
        "what_you_learn": "Master cd command, directory navigation, and path shortcuts (~, -, ..)",
        "objective": "Master cd command and directory navigation",
        "category": "Beginner",
        "difficulty": 1,
        "hint": "Use 'cd' to change directories, '..' to go up",
        "flag": "CTF{navigation_pro_2024}",
        "tasks": [
            {"instruction": 'Use `cd ~` to move to your personal home directory.', "check": "cd ~"},
            {"instruction": 'Use `cd /` to move to the Linux root directory, which is the top of the filesystem.', "check": "cd /"},
            {"instruction": 'Use `cd -` to return to the directory you were in just before the current one.', "check": "cd -"},
            {"instruction": 'Use `cd ..` to move up to the parent directory.', "check": "cd .."},
            {"instruction": "Go to /var/log directory", "check": "cd /var/log"},
            {"instruction": "Go to /etc directory", "check": "cd /etc"}
        ]
    },
    3: {
        "name": "📁 Directory Creator",
        "description": "Create and manage directories",
        "what_you_learn": "Create directories with mkdir, including nested directories with -p flag",
        "objective": "Learn mkdir and directory operations",
        "category": "Beginner",
        "difficulty": 1,
        "hint": "mkdir creates directories, -p creates parent directories",
        "flag": "CTF{dir_creator_2024}",
        "tasks": [
            {"instruction": 'Create a new folder named `projects` using `mkdir`.', "check": "mkdir projects"},
            {"instruction": 'Create a new folder named `temp` using `mkdir`.', "check": "mkdir temp"},
            {"instruction": 'Create the complete folder path `a/b/c`, including any parent folders that do not already exist.', "check": "mkdir -p a/b/c"},
            {"instruction": 'Create a folder named `My Documents`. Remember that spaces must be handled correctly in the command.', "check": "mkdir 'My Documents'"},
            {"instruction": 'Create three folders named `dir1`, `dir2`, and `dir3` with a single command.', "check": "mkdir dir1 dir2 dir3"}
        ]
    },
    4: {
        "name": "📝 File Creation",
        "description": "Create files using different methods",
        "what_you_learn": "Create files using touch, echo, cat and understanding redirection (>, >>)",
        "objective": "Learn touch, echo, and cat commands",
        "category": "Beginner",
        "difficulty": 1,
        "hint": "touch creates empty files, echo writes content",
        "flag": "CTF{file_creator_pro}",
        "tasks": [
            {"instruction": 'Create an empty file named `notes.txt` using a suitable Linux command.', "check": "touch notes.txt"},
            {"instruction": 'Create three empty files named `file1.txt`, `file2.txt`, and `file3.txt` in one command.', "check": "touch file1.txt file2.txt file3.txt"},
            {"instruction": 'Create or overwrite `hello.txt` so that it contains the text `Hello World`.', "check": "echo 'Hello World' > hello.txt"},
            {"instruction": 'Add `Welcome to Linux` to the end of `hello.txt` without deleting its existing contents.', "check": "echo 'Welcome to Linux' >> hello.txt"},
            {"instruction": "Create file using cat redirection", "check": "cat > data.txt << EOF"}
        ]
    },
    5: {
        "name": "👀 Viewing Files",
        "description": "View file contents in different ways",
        "what_you_learn": "View files with cat, head, tail, less and real-time monitoring with tail -f",
        "objective": "Learn cat, head, tail, less commands",
        "category": "Beginner",
        "difficulty": 2,
        "hint": "head shows beginning, tail shows end of files",
        "flag": "CTF{viewer_expert}",
        "tasks": [
            {"instruction": 'Display all of the text inside `file.txt`.', "check": "cat file.txt"},
            {"instruction": 'Display the first 10 lines of `log.txt`.', "check": "head log.txt"},
            {"instruction": 'Display the first 20 lines of `data.txt`.', "check": "head -20 data.txt"},
            {"instruction": 'Display the last 10 lines of `syslog`.', "check": "tail syslog"},
            {"instruction": 'Display the last 50 lines of `syslog`.', "check": "tail -50 syslog"},
            {"instruction": 'Watch `app.log` continuously so that new lines appear as they are added.', "check": "tail -f app.log"},
            {"instruction": 'Open `longfile.txt` one screen at a time so you can read a large file comfortably.', "check": "less longfile.txt"}
        ]
    },
    6: {
        "name": "📋 Copy & Move",
        "description": "Learn to copy and move files",
        "what_you_learn": "Copy files with cp, move/rename with mv, and understanding recursive operations",
        "objective": "Master cp and mv commands",
        "category": "Beginner",
        "difficulty": 2,
        "hint": "cp copies, mv moves/renames files",
        "flag": "CTF{copy_move_master}",
        "tasks": [
            {"instruction": 'Create a copy of `file1.txt` named `file2.txt`.', "check": "cp file1.txt file2.txt"},
            {"instruction": 'Copy every `.txt` file in the current directory into the `backup/` folder.', "check": "cp *.txt backup/"},
            {"instruction": 'Copy the entire `source_dir/` folder, including its contents, into `dest_dir/`.', "check": "cp -r source_dir/ dest_dir/"},
            {"instruction": "Copy with preservation of attributes", "check": "cp -p file.txt file_copy.txt"},
            {"instruction": 'Move `file.txt` into the `/tmp/` directory.', "check": "mv file.txt /tmp/"},
            {"instruction": 'Rename `oldname.txt` to `newname.txt`.', "check": "mv oldname.txt newname.txt"},
            {"instruction": "Move multiple files to directory", "check": "mv file1.txt file2.txt destination/"}
        ]
    },
    7: {
        "name": "🗑️ Remove & Clean",
        "description": "Safely remove files and directories",
        "what_you_learn": "Safely remove files with rm, remove directories with rmdir, and force deletion",
        "objective": "Learn rm, rmdir, and safe deletion",
        "category": "Beginner",
        "difficulty": 2,
        "hint": "rm removes files, rmdir removes empty directories",
        "flag": "CTF{clean_master_2024}",
        "tasks": [
            {"instruction": 'Delete the file named `temp.log`.', "check": "rm temp.log"},
            {"instruction": 'Delete `test.txt`, but make Linux ask you for confirmation first.', "check": "rm -i test.txt"},
            {"instruction": 'Delete the empty folder named `empty`.', "check": "rmdir empty"},
            {"instruction": 'Delete `old_folder` and everything inside it.', "check": "rm -rf old_folder"},
            {"instruction": 'Force-delete `force_delete.txt` without asking for confirmation.', "check": "rm -f force_delete.txt"},
            {"instruction": 'Delete `file1.txt`, `file2.txt`, and `file3.txt` with one command.', "check": "rm file1.txt file2.txt file3.txt"},
            {"instruction": 'Delete every file ending in `.tmp` in the current directory.', "check": "rm *.tmp"}
        ]
    },
    8: {
        "name": "🎯 Wildcards & Patterns",
        "description": "Use wildcards to work with multiple files",
        "what_you_learn": "Use wildcards (*, ?, []) to match and manipulate multiple files efficiently",
        "objective": "Master *, ?, [] wildcards",
        "category": "Beginner",
        "difficulty": 2,
        "hint": "* matches any characters, ? matches single character",
        "flag": "CTF{wildcard_expert}",
        "tasks": [
            {"instruction": 'Display every file whose name ends with `.txt`.', "check": "ls *.txt"},
            {"instruction": 'Display files whose names begin with the letter `a`.', "check": "ls a*"},
            {"instruction": 'Display filenames that contain exactly five characters.', "check": "ls ?????"},
            {"instruction": "List files ending with .log or .txt", "check": "ls *.{log,txt}"},
            {"instruction": "Remove all .bak files", "check": "rm *.bak"},
            {"instruction": "Copy all .conf files to backup/", "check": "cp *.conf backup/"},
            {"instruction": "List files with numbers 1-5", "check": "ls file[1-5].txt"}
        ]
    },
    9: {
        "name": "🔍 Search with grep",
        "description": "Search for patterns in files",
        "what_you_learn": "Search text with grep, use options like -i, -r, -n, -w for powerful searches",
        "objective": "Learn grep and its options",
        "category": "Beginner",
        "difficulty": 3,
        "hint": "grep searches text, -i for case-insensitive",
        "flag": "CTF{grep_master_2024}",
        "tasks": [
            {"instruction": 'Search `log.txt` and display lines containing the word `error`.', "check": "grep error log.txt"},
            {"instruction": 'Search for `warning` in `log.txt` without caring whether it is uppercase or lowercase.', "check": "grep -i warning log.txt"},
            {"instruction": 'Search through the current directory and its subdirectories for the text `TODO`.', "check": "grep -r TODO ."},
            {"instruction": 'Search `file.txt` for `pattern` and include the matching line numbers.', "check": "grep -n pattern file.txt"},
            {"instruction": 'Search `code.txt` for the complete word `main`, not words that merely contain `main`.', "check": "grep -w 'main' code.txt"},
            {"instruction": "Search for multiple patterns", "check": "grep -e error -e warning log.txt"},
            {"instruction": "Search and show context (2 lines before/after)", "check": "grep -C 2 error log.txt"},
            {"instruction": "Search excluding certain files", "check": "grep -r --exclude=*.log pattern ."}
        ]
    },
    10: {
        "name": "🔎 Find Files",
        "description": "Find files and directories",
        "what_you_learn": "Use find command to search by name, type, size, and modification time",
        "objective": "Master find command",
        "category": "Beginner",
        "difficulty": 3,
        "hint": "find searches for files, -name for name pattern",
        "flag": "CTF{finder_expert}",
        "tasks": [
            {"instruction": 'Use `find` to locate all `.txt` files starting from the current directory.', "check": "find . -name '*.txt'"},
            {"instruction": 'Use `find` to locate files whose names contain `conf`.', "check": "find . -name '*conf*'"},
            {"instruction": 'Use `find` to locate files that were modified within the last 7 days.', "check": "find . -mtime -7"},
            {"instruction": 'Use `find` to locate files modified within the last 24 hours.', "check": "find . -mtime -1"},
            {"instruction": 'Use `find` to locate files larger than 10 MB.', "check": "find . -size +10M"},
            {"instruction": 'Use `find` to locate files smaller than 1 KB.', "check": "find . -size -1k"},
            {"instruction": 'Use `find` to locate empty files and directories.', "check": "find . -empty"},
            {"instruction": 'Use `find` to locate directories only, excluding regular files.', "check": "find . -type d"},
            {"instruction": "Find files and execute command", "check": "find . -name '*.txt' -exec ls -l {} \\;"}
        ]
    },
    11: {
        "name": "🔐 File Permissions",
        "description": "Understanding and changing file permissions",
        "what_you_learn": "Understanding rwx permissions, chmod with numbers and symbols, chown for ownership",
        "objective": "Learn chmod, chown, and permission basics",
        "category": "Intermediate",
        "difficulty": 3,
        "hint": "chmod with numbers: 755, 644, 400",
        "flag": "CTF{permissions_expert}",
        "tasks": [
            {"instruction": 'Change the permissions of `script.sh` so the file owner can execute it.', "check": "chmod u+x script.sh"},
            {"instruction": 'Set `file.txt` to permission mode `755` (owner can read/write/execute; group and others can read/execute).', "check": "chmod 755 file.txt"},
            {"instruction": 'Set `data.txt` to permission mode `644` (owner can read/write; everyone else can read).', "check": "chmod 644 data.txt"},
            {"instruction": 'Set `secret.txt` so that only the owner has read permission.', "check": "chmod 400 secret.txt"},
            {"instruction": 'Set `private.txt` so that only the owner can read and write it.', "check": "chmod 600 private.txt"},
            {"instruction": "Add write permission for group", "check": "chmod g+w file.txt"},
            {"instruction": "Remove read permission for others", "check": "chmod o-r file.txt"},
            {"instruction": "Change file owner", "check": "chown user:group file.txt"},
            {"instruction": "Change file group only", "check": "chown :group file.txt"},
            {"instruction": "Apply permissions recursively", "check": "chmod -R 755 /path/dir"}
        ]
    },
    12: {
        "name": "🔗 Links & Shortcuts",
        "description": "Create and manage symbolic and hard links",
        "what_you_learn": "Create symbolic links (shortcuts) with ln -s and understand hard links",
        "objective": "Understand soft and hard links",
        "category": "Intermediate",
        "difficulty": 3,
        "hint": "ln -s creates symbolic link",
        "flag": "CTF{link_master_2024}",
        "tasks": [
            {"instruction": "Create symbolic link to file.txt", "check": "ln -s file.txt link.txt"},
            {"instruction": "Create symbolic link to directory", "check": "ln -s /home/user/Documents docs"},
            {"instruction": "Create hard link to data.txt", "check": "ln data.txt hardlink.txt"},
            {"instruction": "List all links in directory", "check": "ls -l | grep '^l'"},
            {"instruction": "Update existing symbolic link", "check": "ln -sf new_file.txt link.txt"},
            {"instruction": "Find all symbolic links", "check": "find . -type l"},
            {"instruction": "View link details", "check": "readlink link.txt"}
        ]
    },
    13: {
        "name": "📤 I/O Redirection",
        "description": "Redirect input and output",
        "what_you_learn": "Redirect stdout with >, >>, stderr with 2>, and pipes | for chaining commands",
        "objective": "Master redirection and pipes",
        "category": "Intermediate",
        "difficulty": 3,
        "hint": "> overwrites, >> appends, 2> redirects errors",
        "flag": "CTF{redirection_master}",
        "tasks": [
            {"instruction": "Write output to file.txt", "check": "echo 'Hello' > file.txt"},
            {"instruction": "Append output to file.txt", "check": "echo 'World' >> file.txt"},
            {"instruction": "Redirect error to error.log", "check": "command 2> error.log"},
            {"instruction": "Redirect both stdout and stderr", "check": "command > output.txt 2>&1"},
            {"instruction": "Use pipe to filter output", "check": "ls -la | grep .txt"},
            {"instruction": "Pipe multiple commands", "check": "cat file.txt | grep error | wc -l"},
            {"instruction": "Use tee to split output", "check": "echo 'Hello' | tee file.txt"},
            {"instruction": "Redirect to /dev/null", "check": "command > /dev/null 2>&1"}
        ]
    },
    14: {
        "name": "📝 Text Processing",
        "description": "Advanced text manipulation tools",
        "what_you_learn": "Use sed for search/replace, awk for column extraction, cut, sort, uniq, wc",
        "objective": "Master sed, awk, cut, sort, uniq",
        "category": "Intermediate",
        "difficulty": 4,
        "hint": "sed for replace, awk for columns",
        "flag": "CTF{text_master_2024}",
        "tasks": [
            {"instruction": "Replace 'old' with 'new' in file", "check": "sed -i 's/old/new/g' file.txt"},
            {"instruction": "Delete lines containing 'error'", "check": "sed '/error/d' file.txt"},
            {"instruction": "Print second column from data", "check": "awk '{print $2}' data.txt"},
            {"instruction": "Print lines where column 3 > 100", "check": "awk '$3 > 100' data.txt"},
            {"instruction": "Cut first 10 characters", "check": "cut -c1-10 file.txt"},
            {"instruction": "Cut fields 1 and 3 with delimiter", "check": "cut -f1,3 -d',' data.csv"},
            {"instruction": "Sort file alphabetically", "check": "sort file.txt"},
            {"instruction": "Sort numerically descending", "check": "sort -nr numbers.txt"},
            {"instruction": "Show unique lines", "check": "uniq file.txt"},
            {"instruction": "Count occurrences of each line", "check": "sort file.txt | uniq -c"},
            {"instruction": "Count words, lines, characters", "check": "wc file.txt"},
            {"instruction": "Print specific line with sed", "check": "sed -n '5p' file.txt"}
        ]
    },
    15: {
        "name": "⚙️ Process Management",
        "description": "Monitor and control running processes",
        "what_you_learn": "List processes with ps, monitor with top, kill processes, and manage jobs",
        "objective": "Learn ps, top, kill, and process signals",
        "category": "Intermediate",
        "difficulty": 4,
        "hint": "ps aux shows all processes, kill sends signals",
        "flag": "CTF{process_controller}",
        "tasks": [
            {"instruction": "List all running processes", "check": "ps aux"},
            {"instruction": "Show process hierarchy", "check": "ps -ef --forest"},
            {"instruction": "List processes with CPU usage", "check": "ps aux --sort=-%cpu"},
            {"instruction": "List processes by memory usage", "check": "ps aux --sort=-%mem"},
            {"instruction": "Show real-time process monitoring", "check": "top"},
            {"instruction": "Kill process with PID 1234", "check": "kill 1234"},
            {"instruction": "Force kill process", "check": "kill -9 1234"},
            {"instruction": "Send SIGTERM signal", "check": "kill -15 1234"},
            {"instruction": "Send SIGSTOP to pause process", "check": "kill -STOP 1234"},
            {"instruction": "Send SIGCONT to resume process", "check": "kill -CONT 1234"},
            {"instruction": "Start process in background", "check": "command &"},
            {"instruction": "Bring background job to foreground", "check": "fg %1"},
            {"instruction": "List background jobs", "check": "jobs"}
        ]
    },
    16: {
        "name": "💻 System Information",
        "description": "Get system and hardware information",
        "what_you_learn": "Check system info with uname, lscpu, free, df, and hardware details",
        "objective": "Learn system information commands",
        "category": "Intermediate",
        "difficulty": 4,
        "hint": "uname shows system info, free shows memory",
        "flag": "CTF{sysinfo_expert}",
        "tasks": [
            {"instruction": "Show system information", "check": "uname -a"},
            {"instruction": "Show kernel version", "check": "uname -r"},
            {"instruction": "Show CPU information", "check": "lscpu"},
            {"instruction": "Show memory usage (human-readable)", "check": "free -h"},
            {"instruction": "Show disk usage (human-readable)", "check": "df -h"},
            {"instruction": "Show disk usage of current directory", "check": "du -sh"},
            {"instruction": "Show disk usage of all directories", "check": "du -sh *"},
            {"instruction": "Show system uptime", "check": "uptime"},
            {"instruction": "Show hostname", "check": "hostname"},
            {"instruction": "Show system date and time", "check": "date"},
            {"instruction": "Show who is logged in", "check": "who"},
            {"instruction": "Show last system reboot", "check": "last reboot | head -1"}
        ]
    },
    17: {
        "name": "🌐 Network Basics",
        "description": "Basic network commands and diagnostics",
        "what_you_learn": "Check connectivity with ping, view network interfaces with ip, check connections with ss",
        "objective": "Learn ping, ip, ss, netstat commands",
        "category": "Intermediate",
        "difficulty": 4,
        "hint": "ping checks connectivity, ip shows interfaces",
        "flag": "CTF{network_basics}",
        "tasks": [
            {"instruction": "Ping google.com 4 times", "check": "ping -c 4 google.com"},
            {"instruction": "Check network interfaces", "check": "ip addr"},
            {"instruction": "Check network connections", "check": "ss -tuln"},
            {"instruction": "Show all listening ports", "check": "netstat -tuln"},
            {"instruction": "Show routing table", "check": "ip route"},
            {"instruction": "Trace route to google.com", "check": "traceroute google.com"},
            {"instruction": "Check DNS resolution", "check": "nslookup google.com"},
            {"instruction": "Show active connections with IPs", "check": "ss -tunap"},
            {"instruction": "Show network statistics", "check": "netstat -i"},
            {"instruction": "Test specific port connectivity", "check": "nc -zv google.com 80"},
            {"instruction": "Show MAC address", "check": "ip link show"},
            {"instruction": "Check network bandwidth", "check": "iftop"}
        ]
    },
    18: {
        "name": "⚡ Advanced Processes",
        "description": "Advanced process control and monitoring",
        "what_you_learn": "Process priorities, signals, background jobs, and process groups",
        "objective": "Master advanced process management",
        "category": "Intermediate",
        "difficulty": 5,
        "hint": "nice changes priority, nohup runs processes that survive logout",
        "flag": "CTF{process_guru_2024}",
        "tasks": [
            {"instruction": "Start process with low priority", "check": "nice -n 19 command"},
            {"instruction": "Start process with high priority", "check": "nice -n -20 command"},
            {"instruction": "Change priority of running process", "check": "renice -n 10 -p 1234"},
            {"instruction": "Run process that survives logout", "check": "nohup command &"},
            {"instruction": "List all processes with nice values", "check": "ps -eo pid,nice,cmd"},
            {"instruction": "Send SIGUSR1 signal to process", "check": "kill -USR1 1234"},
            {"instruction": "Display process tree", "check": "pstree -p"},
            {"instruction": "Show process environment variables", "check": "cat /proc/1234/environ"},
            {"instruction": "Limit process CPU time", "check": "ulimit -t 10"},
            {"instruction": "Limit process memory usage", "check": "ulimit -m 102400"},
            {"instruction": "Show open files for process", "check": "lsof -p 1234"},
            {"instruction": "Show process memory maps", "check": "cat /proc/1234/maps"}
        ]
    },
    19: {
        "name": "🌐 Network Configuration",
        "description": "Configure and manage network interfaces",
        "what_you_learn": "Configure IP addresses, routes, DNS, and network interfaces",
        "objective": "Master network configuration",
        "category": "Intermediate",
        "difficulty": 5,
        "hint": "ifconfig, ip, route, resolve.conf",
        "flag": "CTF{network_config_pro}",
        "tasks": [
            {"instruction": "Show all network interfaces", "check": "ip addr show"},
            {"instruction": "Show interface eth0 details", "check": "ip addr show eth0"},
            {"instruction": "Bring interface up", "check": "ip link set eth0 up"},
            {"instruction": "Bring interface down", "check": "ip link set eth0 down"},
            {"instruction": "Add IP address to interface", "check": "ip addr add 192.168.1.100/24 dev eth0"},
            {"instruction": "Remove IP address from interface", "check": "ip addr del 192.168.1.100/24 dev eth0"},
            {"instruction": "Show routing table", "check": "ip route show"},
            {"instruction": "Add default gateway", "check": "ip route add default via 192.168.1.1"},
            {"instruction": "Delete route", "check": "ip route del 192.168.2.0/24"},
            {"instruction": "Show ARP table", "check": "ip neigh show"},
            {"instruction": "Flush ARP cache", "check": "ip neigh flush all"},
            {"instruction": "Show DNS configuration", "check": "cat /etc/resolv.conf"},
            {"instruction": "Add DNS server", "check": "echo 'nameserver 8.8.8.8' >> /etc/resolv.conf"}
        ]
    },
    20: {
        "name": "🛡️ Firewall Management",
        "description": "Configure and manage firewall rules",
        "what_you_learn": "iptables, ufw, and firewall basics",
        "objective": "Master firewall configuration",
        "category": "Intermediate",
        "difficulty": 6,
        "hint": "iptables for advanced, ufw for simple firewall",
        "flag": "CTF{firewall_expert_2024}",
        "tasks": [
            {"instruction": "Show current iptables rules", "check": "iptables -L -v"},
            {"instruction": "Show NAT table", "check": "iptables -t nat -L"},
            {"instruction": "Allow SSH on port 22", "check": "iptables -A INPUT -p tcp --dport 22 -j ACCEPT"},
            {"instruction": "Allow HTTP on port 80", "check": "iptables -A INPUT -p tcp --dport 80 -j ACCEPT"},
            {"instruction": "Allow HTTPS on port 443", "check": "iptables -A INPUT -p tcp --dport 443 -j ACCEPT"},
            {"instruction": "Block IP address", "check": "iptables -A INPUT -s 192.168.1.100 -j DROP"},
            {"instruction": "Block port 25", "check": "iptables -A INPUT -p tcp --dport 25 -j DROP"},
            {"instruction": "Enable NAT masquerading", "check": "iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE"},
            {"instruction": "Enable UFW", "check": "ufw enable"},
            {"instruction": "Allow SSH via UFW", "check": "ufw allow ssh"},
            {"instruction": "Allow specific port via UFW", "check": "ufw allow 8080/tcp"},
            {"instruction": "Delete rule by number", "check": "iptables -D INPUT 3"}
        ]
    },
    21: {
        "name": "⚙️ Systemd Mastery",
        "description": "Manage services with systemd",
        "what_you_learn": "Systemd, services, units, timers, and journal",
        "objective": "Master systemd service management",
        "category": "Advanced",
        "difficulty": 6,
        "hint": "systemctl, journalctl, service units",
        "flag": "CTF{systemd_master_2024}",
        "tasks": [
            {"instruction": "List all running services", "check": "systemctl list-units --type=service"},
            {"instruction": "List all services (including inactive)", "check": "systemctl list-units --type=service --all"},
            {"instruction": "Start a service", "check": "systemctl start apache2"},
            {"instruction": "Stop a service", "check": "systemctl stop apache2"},
            {"instruction": "Restart a service", "check": "systemctl restart apache2"},
            {"instruction": "Reload service configuration", "check": "systemctl reload apache2"},
            {"instruction": "Enable service at boot", "check": "systemctl enable apache2"},
            {"instruction": "Disable service at boot", "check": "systemctl disable apache2"},
            {"instruction": "Check service status", "check": "systemctl status apache2"},
            {"instruction": "Show service logs", "check": "journalctl -u apache2"},
            {"instruction": "Show system logs since last boot", "check": "journalctl -b"},
            {"instruction": "Follow journal in real-time", "check": "journalctl -f"},
            {"instruction": "Show service dependencies", "check": "systemctl list-dependencies apache2"},
            {"instruction": "Create a new service unit", "check": "systemctl edit --force myapp.service"}
        ]
    },
    22: {
        "name": "📦 Package Management",
        "description": "Manage software packages on Linux",
        "what_you_learn": "apt, dpkg, yum, dnf for package management",
        "objective": "Master package management",
        "category": "Advanced",
        "difficulty": 5,
        "hint": "apt for Debian/Ubuntu, yum for RHEL/CentOS",
        "flag": "CTF{package_master_2024}",
        "tasks": [
            {"instruction": "Update package lists", "check": "apt update"},
            {"instruction": "Upgrade all packages", "check": "apt upgrade"},
            {"instruction": "Install a package", "check": "apt install nginx"},
            {"instruction": "Remove a package", "check": "apt remove nginx"},
            {"instruction": "Remove package and configuration", "check": "apt purge nginx"},
            {"instruction": "Search for package", "check": "apt search apache"},
            {"instruction": "Show package information", "check": "apt show nginx"},
            {"instruction": "List installed packages", "check": "dpkg -l"},
            {"instruction": "Install .deb package", "check": "dpkg -i package.deb"},
            {"instruction": "Show package contents", "check": "dpkg -L nginx"},
            {"instruction": "Check package dependencies", "check": "apt-cache depends nginx"},
            {"instruction": "Fix broken dependencies", "check": "apt-get install -f"},
            {"instruction": "Download package without install", "check": "apt download nginx"},
            {"instruction": "Clean package cache", "check": "apt autoclean"}
        ]
    },
    23: {
        "name": "💾 Disk Management",
        "description": "Manage disks, partitions, and filesystems",
        "what_you_learn": "fdisk, parted, mkfs, mount, and disk utilities",
        "objective": "Master disk and filesystem management",
        "category": "Advanced",
        "difficulty": 6,
        "hint": "fdisk for partitioning, mkfs for filesystem creation",
        "flag": "CTF{disk_master_2024}",
        "tasks": [
            {"instruction": "List all disks and partitions", "check": "fdisk -l"},
            {"instruction": "List disk usage", "check": "df -h"},
            {"instruction": "Show disk usage of directory", "check": "du -sh /home"},
            {"instruction": "Show disk usage with details", "check": "du -ach /home"},
            {"instruction": "Create filesystem on partition", "check": "mkfs.ext4 /dev/sdb1"},
            {"instruction": "Mount partition", "check": "mount /dev/sdb1 /mnt/data"},
            {"instruction": "Unmount partition", "check": "umount /mnt/data"},
            {"instruction": "Check filesystem", "check": "fsck /dev/sdb1"},
            {"instruction": "Show mounted filesystems", "check": "mount"},
            {"instruction": "Show partition table", "check": "parted -l"},
            {"instruction": "Create new partition", "check": "parted /dev/sdb mkpart primary ext4 0 10GB"},
            {"instruction": "Format with swap", "check": "mkswap /dev/sdb2"},
            {"instruction": "Enable swap", "check": "swapon /dev/sdb2"},
            {"instruction": "Show UUIDs of filesystems", "check": "blkid"}
        ]
    },
    24: {
        "name": "📊 LVM Management",
        "description": "Logical Volume Manager operations",
        "what_you_learn": "PV, VG, LV creation, extension, and snapshot",
        "objective": "Master LVM administration",
        "category": "Advanced",
        "difficulty": 7,
        "hint": "pvcreate, vgcreate, lvcreate for LVM",
        "flag": "CTF{lvm_master_2024}",
        "tasks": [
            {"instruction": "Show physical volumes", "check": "pvdisplay"},
            {"instruction": "Create physical volume", "check": "pvcreate /dev/sdb"},
            {"instruction": "Show volume groups", "check": "vgdisplay"},
            {"instruction": "Create volume group", "check": "vgcreate vg_data /dev/sdb"},
            {"instruction": "Show logical volumes", "check": "lvdisplay"},
            {"instruction": "Create logical volume", "check": "lvcreate -n lv_data -L 10G vg_data"},
            {"instruction": "Extend logical volume", "check": "lvextend -L +5G /dev/vg_data/lv_data"},
            {"instruction": "Reduce logical volume", "check": "lvreduce -L -5G /dev/vg_data/lv_data"},
            {"instruction": "Create LVM snapshot", "check": "lvcreate -s -n snap1 -L 1G /dev/vg_data/lv_data"},
            {"instruction": "Show LVM info", "check": "lvs"},
            {"instruction": "Add disk to volume group", "check": "vgextend vg_data /dev/sdc"},
            {"instruction": "Remove disk from volume group", "check": "vgreduce vg_data /dev/sdc"},
            {"instruction": "Activate all LVM volumes", "check": "vgchange -ay"},
            {"instruction": "Deactivate all LVM volumes", "check": "vgchange -an"}
        ]
    },
    25: {
        "name": "🔄 RAID Configuration",
        "description": "Configure and manage software RAID",
        "what_you_learn": "RAID levels, mdadm, and software RAID management",
        "objective": "Master software RAID administration",
        "category": "Advanced",
        "difficulty": 7,
        "hint": "mdadm for software RAID management",
        "flag": "CTF{raid_master_2024}",
        "tasks": [
            {"instruction": "Create RAID 0 array", "check": "mdadm --create /dev/md0 --level=0 --raid-devices=2 /dev/sdb1 /dev/sdc1"},
            {"instruction": "Create RAID 1 array", "check": "mdadm --create /dev/md1 --level=1 --raid-devices=2 /dev/sdb1 /dev/sdc1"},
            {"instruction": "Create RAID 5 array", "check": "mdadm --create /dev/md5 --level=5 --raid-devices=3 /dev/sdb1 /dev/sdc1 /dev/sdd1"},
            {"instruction": "Show RAID status", "check": "mdadm --detail /dev/md0"},
            {"instruction": "List all RAID arrays", "check": "cat /proc/mdstat"},
            {"instruction": "Add disk to RAID", "check": "mdadm --add /dev/md0 /dev/sdd1"},
            {"instruction": "Remove disk from RAID", "check": "mdadm --remove /dev/md0 /dev/sdb1"},
            {"instruction": "Fail a disk in RAID", "check": "mdadm --fail /dev/md0 /dev/sdb1"},
            {"instruction": "Stop RAID array", "check": "mdadm --stop /dev/md0"},
            {"instruction": "Assemble RAID array", "check": "mdadm --assemble /dev/md0 /dev/sdb1 /dev/sdc1"},
            {"instruction": "Save RAID configuration", "check": "mdadm --detail --scan >> /etc/mdadm/mdadm.conf"}
        ]
    },
    26: {
        "name": "🔑 SSH & Remote Access",
        "description": "Secure Shell configuration and usage",
        "what_you_learn": "SSH client, server configuration, key management, tunneling",
        "objective": "Master SSH for remote access",
        "category": "Advanced",
        "difficulty": 6,
        "hint": "ssh, sshd_config, ssh-keygen",
        "flag": "CTF{ssh_master_2024}",
        "tasks": [
            {"instruction": "Connect to remote server", "check": "ssh user@192.168.1.100"},
            {"instruction": "Connect on custom port", "check": "ssh -p 2222 user@192.168.1.100"},
            {"instruction": "Generate SSH key pair", "check": "ssh-keygen -t rsa -b 4096"},
            {"instruction": "Copy SSH key to server", "check": "ssh-copy-id user@192.168.1.100"},
            {"instruction": "Disable password authentication", "check": "echo 'PasswordAuthentication no' >> /etc/ssh/sshd_config"},
            {"instruction": "Disable root login", "check": "echo 'PermitRootLogin no' >> /etc/ssh/sshd_config"},
            {"instruction": "Change SSH default port", "check": "echo 'Port 2222' >> /etc/ssh/sshd_config"},
            {"instruction": "Create SSH config for host", "check": "echo 'Host myserver\n  HostName 192.168.1.100\n  User admin' >> ~/.ssh/config"},
            {"instruction": "Set up SSH tunneling", "check": "ssh -L 8080:localhost:80 user@server"},
            {"instruction": "Set up SOCKS proxy", "check": "ssh -D 1080 user@server"},
            {"instruction": "Copy file via SSH", "check": "scp file.txt user@server:/path/"},
            {"instruction": "Mount remote directory via SSH", "check": "sshfs user@server:/path /mnt/remote"},
            {"instruction": "Restart SSH service", "check": "systemctl restart sshd"},
            {"instruction": "Show SSH connection status", "check": "netstat -tunap | grep ssh"}
        ]
    },
    27: {
        "name": "🌐 Web Server Administration",
        "description": "Configure and manage web servers",
        "what_you_learn": "Apache/Nginx configuration, virtual hosts, SSL/TLS",
        "objective": "Master web server administration",
        "category": "Advanced",
        "difficulty": 7,
        "hint": "a2ensite, a2dissite, nginx configuration",
        "flag": "CTF{web_admin_2024}",
        "tasks": [
            {"instruction": "Install Apache web server", "check": "apt install apache2"},
            {"instruction": "Start Apache service", "check": "systemctl start apache2"},
            {"instruction": "Check Apache status", "check": "systemctl status apache2"},
            {"instruction": "Enable Apache module", "check": "a2enmod rewrite"},
            {"instruction": "Create virtual host", "check": "a2ensite mywebsite.conf"},
            {"instruction": "Disable default site", "check": "a2dissite 000-default.conf"},
            {"instruction": "Reload Apache configuration", "check": "systemctl reload apache2"},
            {"instruction": "Install Nginx", "check": "apt install nginx"},
            {"instruction": "Test Nginx configuration", "check": "nginx -t"},
            {"instruction": "Create SSL certificate", "check": "openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365"},
            {"instruction": "Enable HTTPS in Apache", "check": "a2enmod ssl"},
            {"instruction": "Set up reverse proxy", "check": "echo 'proxy_pass http://localhost:3000;' >> /etc/nginx/sites-available/default"},
            {"instruction": "Configure load balancing", "check": "echo 'upstream backend { server 10.0.0.1; server 10.0.0.2; }' >> /etc/nginx/nginx.conf"},
            {"instruction": "Set up Gzip compression", "check": "echo 'gzip on;' >> /etc/nginx/nginx.conf"}
        ]
    },
    28: {
        "name": "💾 Database Administration",
        "description": "Manage MySQL/PostgreSQL databases",
        "what_you_learn": "Database creation, backup, restore, user management",
        "objective": "Master database administration",
        "category": "Advanced",
        "difficulty": 7,
        "hint": "mysql, mysqldump, psql, createdb",
        "flag": "CTF{db_admin_2024}",
        "tasks": [
            {"instruction": "Install MySQL server", "check": "apt install mysql-server"},
            {"instruction": "Connect to MySQL", "check": "mysql -u root -p"},
            {"instruction": "Show all databases", "check": "mysql -e 'SHOW DATABASES;'"},
            {"instruction": "Create new database", "check": "mysql -e 'CREATE DATABASE mydb;'"},
            {"instruction": "Create MySQL user", "check": "mysql -e \"CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';\""},
            {"instruction": "Grant privileges", "check": "mysql -e \"GRANT ALL PRIVILEGES ON mydb.* TO 'user'@'localhost';\""},
            {"instruction": "Import SQL file", "check": "mysql -u root -p mydb < backup.sql"},
            {"instruction": "Export database", "check": "mysqldump -u root -p mydb > backup.sql"},
            {"instruction": "Install PostgreSQL", "check": "apt install postgresql"},
            {"instruction": "Connect to PostgreSQL", "check": "psql -U postgres"},
            {"instruction": "Create PostgreSQL database", "check": "createdb mydb"},
            {"instruction": "List PostgreSQL databases", "check": "psql -l"},
            {"instruction": "Create PostgreSQL user", "check": "createuser -U postgres myuser"},
            {"instruction": "Import PostgreSQL dump", "check": "psql -U postgres mydb < backup.sql"}
        ]
    },
    29: {
        "name": "📜 Shell Scripting Basics",
        "description": "Create and run shell scripts",
        "what_you_learn": "Variables, conditionals, loops, functions in bash",
        "objective": "Master basic shell scripting",
        "category": "Advanced",
        "difficulty": 6,
        "hint": "#!/bin/bash, variables, if statements, for loops",
        "flag": "CTF{scripting_basics}",
        "tasks": [
            {"instruction": "Create hello world script", "check": "echo '#!/bin/bash' > hello.sh && echo 'echo \"Hello World\"' >> hello.sh"},
            {"instruction": "Make script executable", "check": "chmod +x hello.sh"},
            {"instruction": "Create script with variables", "check": "echo 'NAME=\"John\" && echo \"Hello $NAME\"' > var.sh"},
            {"instruction": "Use if-else in script", "check": "echo 'if [ -f file.txt ]; then echo \"exists\"; else echo \"missing\"; fi' > condition.sh"},
            {"instruction": "Create for loop in script", "check": "echo 'for i in {1..5}; do echo $i; done' > loop.sh"},
            {"instruction": "Use while loop", "check": "echo 'count=1; while [ $count -le 5 ]; do echo $count; ((count++)); done' > while.sh"},
            {"instruction": "Create function in script", "check": "echo 'function greet() { echo \"Hello\"; }' > func.sh"},
            {"instruction": "Use case statement", "check": "echo 'case $1 in start) echo \"starting\";; stop) echo \"stopping\";; esac' > case.sh"},
            {"instruction": "Create script with arguments", "check": "echo 'echo \"First arg: $1\"' > args.sh"},
            {"instruction": "Use arrays in script", "check": "echo 'arr=(\"a\" \"b\" \"c\"); for i in ${arr[@]}; do echo $i; done' > array.sh"},
            {"instruction": "Add error handling", "check": "echo 'set -e' > error.sh && echo 'ls non_existent' >> error.sh"},
            {"instruction": "Read user input in script", "check": "echo 'read -p \"Enter name: \" name; echo \"Hello $name\"' > input.sh"}
        ]
    },
    30: {
        "name": "🚀 Advanced Scripting",
        "description": "Advanced shell scripting techniques",
        "what_you_learn": "Regular expressions, sed, awk, xargs, parallel processing",
        "objective": "Master advanced scripting",
        "category": "Advanced",
        "difficulty": 7,
        "hint": "sed for streaming, awk for data processing",
        "flag": "CTF{advanced_scripting}",
        "tasks": [
            {"instruction": "Use sed to replace in file", "check": "sed -i 's/old/new/g' file.txt"},
            {"instruction": "Use sed to delete lines", "check": "sed '/pattern/d' file.txt"},
            {"instruction": "Use awk to print specific columns", "check": "awk '{print $1, $3}' data.txt"},
            {"instruction": "Use awk with conditions", "check": "awk '$3 > 100 {print $1}' data.txt"},
            {"instruction": "Use xargs to process output", "check": "ls *.txt | xargs rm"},
            {"instruction": "Use xargs with multiple arguments", "check": "find . -name '*.log' | xargs -I {} cp {} /backup/"},
            {"instruction": "Use parallel processing", "check": "ls *.sh | parallel bash {}"},
            {"instruction": "Use grep with regex", "check": "grep '^[0-9]' file.txt"},
            {"instruction": "Use cut to extract fields", "check": "cut -d',' -f2 data.csv"},
            {"instruction": "Combine multiple commands", "check": "cat file.txt | grep error | wc -l"},
            {"instruction": "Use here document", "check": "cat << EOF > file.txt\nThis is a here document\nEOF"},
            {"instruction": "Use trap for signals", "check": "echo 'trap \"echo Exit\" EXIT' > trap.sh"}
        ]
    },
    31: {
        "name": "📡 DNS & Bind",
        "description": "Configure and manage DNS server",
        "what_you_learn": "BIND configuration, zone files, DNS records",
        "objective": "Master DNS server administration",
        "category": "Expert",
        "difficulty": 8,
        "hint": "named, zone files, dig, nslookup",
        "flag": "CTF{dns_master_2024}",
        "tasks": [
            {"instruction": "Install BIND DNS server", "check": "apt install bind9"},
            {"instruction": "Start BIND service", "check": "systemctl start named"},
            {"instruction": "Check BIND status", "check": "systemctl status named"},
            {"instruction": "Query DNS server", "check": "dig @localhost example.com"},
            {"instruction": "Lookup domain", "check": "nslookup example.com"},
            {"instruction": "Create zone file", "check": "echo '$TTL 86400\n@ IN SOA ns1.example.com. admin.example.com. (2024061701 3600 1800 604800 86400)' > /etc/bind/db.example.com"},
            {"instruction": "Add A record", "check": "echo 'www IN A 192.168.1.100' >> /etc/bind/db.example.com"},
            {"instruction": "Add CNAME record", "check": "echo 'ftp IN CNAME www' >> /etc/bind/db.example.com"},
            {"instruction": "Add MX record", "check": "echo '@ IN MX 10 mail.example.com' >> /etc/bind/db.example.com"},
            {"instruction": "Add reverse record", "check": "echo '100 IN PTR www.example.com' >> /etc/bind/db.192.168.1"},
            {"instruction": "Test configuration", "check": "named-checkzone example.com /etc/bind/db.example.com"},
            {"instruction": "Reload BIND configuration", "check": "rndc reload"},
            {"instruction": "Enable recursion", "check": "echo 'recursion yes;' >> /etc/bind/named.conf.options"},
            {"instruction": "Set up DNS forwarding", "check": "echo 'forwarders { 8.8.8.8; };' >> /etc/bind/named.conf.options"}
        ]
    },
    32: {
        "name": "🔄 DHCP Server",
        "description": "Configure DHCP server for IP allocation",
        "what_you_learn": "DHCP configuration, subnetting, IP address management",
        "objective": "Master DHCP server administration",
        "category": "Expert",
        "difficulty": 7,
        "hint": "isc-dhcp-server, dhcpd.conf",
        "flag": "CTF{dhcp_master_2024}",
        "tasks": [
            {"instruction": "Install DHCP server", "check": "apt install isc-dhcp-server"},
            {"instruction": "Configure DHCP pool", "check": "echo 'subnet 192.168.1.0 netmask 255.255.255.0 { range 192.168.1.100 192.168.1.200; }' >> /etc/dhcp/dhcpd.conf"},
            {"instruction": "Set DNS servers in DHCP", "check": "echo 'option domain-name-servers 8.8.8.8, 8.8.4.4;' >> /etc/dhcp/dhcpd.conf"},
            {"instruction": "Set default gateway", "check": "echo 'option routers 192.168.1.1;' >> /etc/dhcp/dhcpd.conf"},
            {"instruction": "Set domain name", "check": "echo 'option domain-name \"example.com\";' >> /etc/dhcp/dhcpd.conf"},
            {"instruction": "Create DHCP reservation", "check": "echo 'host client1 { hardware ethernet 00:11:22:33:44:55; fixed-address 192.168.1.10; }' >> /etc/dhcp/dhcpd.conf"},
            {"instruction": "Set DHCP lease time", "check": "echo 'default-lease-time 600;' >> /etc/dhcp/dhcpd.conf"},
            {"instruction": "Set max lease time", "check": "echo 'max-lease-time 7200;' >> /etc/dhcp/dhcpd.conf"},
            {"instruction": "Start DHCP service", "check": "systemctl start isc-dhcp-server"},
            {"instruction": "Check DHCP status", "check": "systemctl status isc-dhcp-server"},
            {"instruction": "View DHCP leases", "check": "cat /var/lib/dhcp/dhcpd.leases"},
            {"instruction": "Restart DHCP service", "check": "systemctl restart isc-dhcp-server"},
            {"instruction": "Enable DHCP at boot", "check": "systemctl enable isc-dhcp-server"}
        ]
    },
    33: {
        "name": "📁 File Sharing",
        "description": "Configure NFS and Samba file sharing",
        "what_you_learn": "NFS exports, Samba configuration, file sharing protocols",
        "objective": "Master file sharing administration",
        "category": "Expert",
        "difficulty": 7,
        "hint": "exports, smb.conf, mount, smbclient",
        "flag": "CTF{fileshare_master}",
        "tasks": [
            {"instruction": "Install NFS server", "check": "apt install nfs-kernel-server"},
            {"instruction": "Create NFS export", "check": "echo '/home/shared *(rw,sync,no_subtree_check)' >> /etc/exports"},
            {"instruction": "Export NFS shares", "check": "exportfs -a"},
            {"instruction": "Show NFS exports", "check": "exportfs -v"},
            {"instruction": "Mount NFS share", "check": "mount -t nfs server:/home/shared /mnt/nfs"},
            {"instruction": "Install Samba server", "check": "apt install samba"},
            {"instruction": "Create Samba share", "check": "echo '[shared]\npath = /home/shared\navailable = yes\nvalid users = user\nread only = no' >> /etc/samba/smb.conf"},
            {"instruction": "Add Samba user", "check": "smbpasswd -a user"},
            {"instruction": "Restart Samba service", "check": "systemctl restart smbd"},
            {"instruction": "Check Samba status", "check": "systemctl status smbd"},
            {"instruction": "List Samba shares", "check": "smbclient -L localhost -U user"},
            {"instruction": "Mount Samba share", "check": "mount -t cifs //server/shared /mnt/samba -o username=user"},
            {"instruction": "Test Samba configuration", "check": "testparm"},
            {"instruction": "Set NFS with no_root_squash", "check": "echo '/home/nfs *(rw,sync,no_root_squash)' >> /etc/exports"}
        ]
    },
    34: {
        "name": "💾 Backup & Recovery",
        "description": "Backup strategies and system recovery",
        "what_you_learn": "rsync, tar, dd, system backup and restore",
        "objective": "Master backup and recovery",
        "category": "Expert",
        "difficulty": 7,
        "hint": "rsync, tar, dd, restore commands",
        "flag": "CTF{backup_master_2024}",
        "tasks": [
            {"instruction": "Create full system backup with tar", "check": "tar -czf backup.tar.gz /"},
            {"instruction": "Backup home directory", "check": "tar -czf home_backup.tar.gz /home/"},
            {"instruction": "Incremental backup with rsync", "check": "rsync -av --progress /source/ /destination/"},
            {"instruction": "Remote backup with rsync", "check": "rsync -avz /local/ user@server:/remote/"},
            {"instruction": "Create disk image with dd", "check": "dd if=/dev/sda of=disk_image.img bs=4M"},
            {"instruction": "Restore disk image", "check": "dd if=disk_image.img of=/dev/sda bs=4M"},
            {"instruction": "Create compressed backup", "check": "tar -czf compressed.tar.gz /data"},
            {"instruction": "Split large backup into parts", "check": "split -b 2G backup.tar.gz backup_part_"},
            {"instruction": "Verify backup integrity", "check": "tar -tzf backup.tar.gz"},
            {"instruction": "Create backup with exclusions", "check": "rsync -av --exclude='*.tmp' /source/ /dest/"},
            {"instruction": "Create system snapshot", "check": "rsync -aAX --delete / /snapshot/"},
            {"instruction": "Create bootable backup", "check": "dd if=/dev/sda of=/backup/boot.img bs=1M count=100"},
            {"instruction": "Backup configuration files", "check": "tar -czf etc_backup.tar.gz /etc/"},
            {"instruction": "Recover specific file from backup", "check": "tar -xzf backup.tar.gz path/to/file"}
        ]
    },
    35: {
        "name": "🐳 Docker Introduction",
        "description": "Getting started with containers",
        "what_you_learn": "Docker installation, images, containers, basic commands",
        "objective": "Master Docker basics",
        "category": "Expert",
        "difficulty": 8,
        "hint": "docker run, ps, images, pull, exec",
        "flag": "CTF{docker_beginner_2024}",
        "tasks": [
            {"instruction": "Check Docker version", "check": "docker --version"},
            {"instruction": "Pull Ubuntu image", "check": "docker pull ubuntu:20.04"},
            {"instruction": "List all images", "check": "docker images"},
            {"instruction": "Run container interactively", "check": "docker run -it ubuntu:20.04 /bin/bash"},
            {"instruction": "Run container in background", "check": "docker run -d nginx"},
            {"instruction": "List running containers", "check": "docker ps"},
            {"instruction": "List all containers", "check": "docker ps -a"},
            {"instruction": "Stop a container", "check": "docker stop container_id"},
            {"instruction": "Start a stopped container", "check": "docker start container_id"},
            {"instruction": "Remove a container", "check": "docker rm container_id"},
            {"instruction": "Remove an image", "check": "docker rmi image_id"},
            {"instruction": "Execute command in running container", "check": "docker exec -it container_id bash"},
            {"instruction": "View container logs", "check": "docker logs container_id"},
            {"instruction": "Inspect container details", "check": "docker inspect container_id"}
        ]
    },
    36: {
        "name": "🐳 Advanced Docker",
        "description": "Advanced container management",
        "what_you_learn": "Dockerfile, volumes, networks, docker-compose",
        "objective": "Master advanced Docker concepts",
        "category": "Expert",
        "difficulty": 8,
        "hint": "Dockerfile, volumes, networks, compose",
        "flag": "CTF{docker_master_2024}",
        "tasks": [
            {"instruction": "Create Dockerfile", "check": "echo 'FROM ubuntu:20.04\\nRUN apt update\\nCMD [\"/bin/bash\"]' > Dockerfile"},
            {"instruction": "Build Docker image", "check": "docker build -t myapp ."},
            {"instruction": "Create volume", "check": "docker volume create mydata"},
            {"instruction": "List volumes", "check": "docker volume ls"},
            {"instruction": "Run container with volume", "check": "docker run -v mydata:/data ubuntu"},
            {"instruction": "Create network", "check": "docker network create mynet"},
            {"instruction": "List networks", "check": "docker network ls"},
            {"instruction": "Run container with network", "check": "docker run --network mynet nginx"},
            {"instruction": "Create docker-compose.yml", "check": "echo 'version: \"3\"\\nservices:\\n  web:\\n    image: nginx\\n    ports:\\n      - \"80:80\"' > docker-compose.yml"},
            {"instruction": "Start with compose", "check": "docker-compose up -d"},
            {"instruction": "Stop with compose", "check": "docker-compose down"},
            {"instruction": "Scale service", "check": "docker-compose scale web=3"},
            {"instruction": "Push image to registry", "check": "docker push username/myalatest"},
            {"instruction": "Save image to file", "check": "docker save -o myimage.tar myapp:latest"}
        ]
    },
    37: {
        "name": "☸️ Kubernetes Introduction",
        "description": "Getting started with Kubernetes",
        "what_you_learn": "kubectl commands, pods, services, deployments",
        "objective": "Master Kubernetes basics",
        "category": "Expert",
        "difficulty": 9,
        "hint": "kubectl get, apply, describe, logs",
        "flag": "CTF{k8s_beginner_2024}",
        "tasks": [
            {"instruction": "Check kubectl version", "check": "kubectl version"},
            {"instruction": "List nodes", "check": "kubectl get nodes"},
            {"instruction": "List all pods", "check": "kubectl get pods --all-namespaces"},
            {"instruction": "Create deployment", "check": "kubectl create deployment nginx --image=nginx"},
            {"instruction": "List deployments", "check": "kubectl get deployments"},
            {"instruction": "Scale deployment", "check": "kubectl scale deployment nginx --replicas=3"},
            {"instruction": "Expose deployment as service", "check": "kubectl expose deployment nginx --port=80 --type=LoadBalancer"},
            {"instruction": "List services", "check": "kubectl get services"},
            {"instruction": "Get pod details", "check": "kubectl describe pod pod-name"},
            {"instruction": "View pod logs", "check": "kubectl logs pod-name"},
            {"instruction": "Execute command in pod", "check": "kubectl exec -it pod-name -- /bin/bash"},
            {"instruction": "Delete deployment", "check": "kubectl delete deployment nginx"},
            {"instruction": "Apply YAML configuration", "check": "kubectl apply -f deployment.yaml"},
            {"instruction": "Port forward to service", "check": "kubectl port-forward service/nginx 8080:80"}
        ]
    },
    38: {
        "name": "☸️ Advanced Kubernetes",
        "description": "Advanced Kubernetes operations",
        "what_you_learn": "ConfigMaps, Secrets, Ingress, Persistent Volumes, Helm",
        "objective": "Master advanced Kubernetes",
        "category": "Expert",
        "difficulty": 9,
        "hint": "configmap, secret, ingress, pv, pvc, helm",
        "flag": "CTF{k8s_master_2024}",
        "tasks": [
            {"instruction": "Create ConfigMap", "check": "kubectl create configmap app-config --from-literal=key=value"},
            {"instruction": "List ConfigMaps", "check": "kubectl get configmaps"},
            {"instruction": "Create Secret", "check": "kubectl create secret generic db-secret --from-literal=password=mypass"},
            {"instruction": "List Secrets", "check": "kubectl get secrets"},
            {"instruction": "Create PersistentVolume", "check": "echo 'apiVersion: v1\\nkind: PersistentVolume\\nmetadata:\\n  name: my-pv\\nspec:\\n  capacity:\\n    storage: 1Gi\\n  accessModes:\\n    - ReadWriteOnce' > pv.yaml && kubectl apply -f pv.yaml"},
            {"instruction": "Create PersistentVolumeClaim", "check": "echo 'apiVersion: v1\\nkind: PersistentVolumeClaim\\nmetadata:\\n  name: my-pvc\\nspec:\\n  accessModes:\\n    - ReadWriteOnce\\n  resources:\\n    requests:\\n      storage: 1Gi' > pvc.yaml && kubectl apply -f pvc.yaml"},
            {"instruction": "Create Ingress resource", "check": "echo 'apiVersion: networking.k8s.io/v1\\nkind: Ingress\\nmetadata:\\n  name: my-ingress\\nspec:\\n  rules:\\n  - host: example.com\\n    http:\\n      paths:\\n      - path: /\\n        pathType: Prefix\\n        backend:\\n          service:\\n            name: nginx\\n            port:\\n              number: 80' > ingress.yaml && kubectl apply -f ingress.yaml"},
            {"instruction": "Install Helm", "check": "curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash"},
            {"instruction": "Add Helm repo", "check": "helm repo add stable https://charts.helm.sh/stable"},
            {"instruction": "Install chart with Helm", "check": "helm install my-release stable/nginx"},
            {"instruction": "List Helm releases", "check": "helm list"},
            {"instruction": "Upgrade Helm release", "check": "helm upgrade my-release stable/nginx --set replicaCount=3"},
            {"instruction": "Uninstall Helm release", "check": "helm uninstall my-release"}
        ]
    },
    39: {
        "name": "🚀 CI/CD Pipeline",
        "description": "Continuous Integration and Deployment",
        "what_you_learn": "Jenkins, GitLab CI, GitHub Actions, pipeline automation",
        "objective": "Master CI/CD pipeline creation",
        "category": "Expert",
        "difficulty": 9,
        "hint": "jenkins, gitlab-ci.yml, github actions",
        "flag": "CTF{ci_cd_master_2024}",
        "tasks": [
            {"instruction": "Install Jenkins", "check": "wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -"},
            {"instruction": "Start Jenkins service", "check": "systemctl start jenkins"},
            {"instruction": "Check Jenkins status", "check": "systemctl status jenkins"},
            {"instruction": "Create Jenkins pipeline", "check": "echo 'pipeline { agent any; stages { stage(\"Build\") { steps { echo \"Building...\" } } } }' > Jenkinsfile"},
            {"instruction": "Create GitLab CI pipeline", "check": "echo 'stages:\\n  - build\\n  - test\\n  - deploy\\nbuild:\\n  stage: build\\n  script:\\n    - echo \"Building...\"' > .gitlab-ci.yml"},
            {"instruction": "Create GitHub Actions workflow", "check": "echo 'name: CI\\non: [push]\\njobs:\\n  build:\\n    runs-on: ubuntu-latest\\n    steps:\\n      - uses: actions/checkout@v2\\n      - name: Run build\\n        run: echo \"Building...\"' > .github/workflows/ci.yml"},
            {"instruction": "Add test stage", "check": "echo 'test:\\n  stage: test\\n  script:\\n    - echo \"Testing...\"' >> .gitlab-ci.yml"},
            {"instruction": "Add deploy stage", "check": "echo 'deploy:\\n  stage: deploy\\n  script:\\n    - echo \"Deploying...\"\\n  only:\\n    - main' >> .gitlab-ci.yml"},
            {"instruction": "Build Docker image in CI", "check": "echo 'build:\\n  stage: build\\n  script:\\n    - docker build -t myapp:$CI_COMMIT_SHA .' >> .gitlab-ci.yml"},
            {"instruction": "Push image to registry", "check": "echo 'push:\\n  stage: build\\n  script:\\n    - docker push myapp:$CI_COMMIT_SHA' >> .gitlab-ci.yml"},
            {"instruction": "Deploy to Kubernetes", "check": "echo 'deploy:\\n  stage: deploy\\n  script:\\n    - kubectl set image deployment/myapp myapp=myapp:$CI_COMMIT_SHA' >> .gitlab-ci.yml"},
            {"instruction": "View Jenkins logs", "check": "tail -f /var/log/jenkins/jenkins.log"},
            {"instruction": "List Jenkins jobs", "check": "jenkins-cli list-jobs"},
            {"instruction": "Create multi-stage pipeline", "check": "echo 'stages:\\n  - build\\n  - test\\n  - deploy\\ninclude:\\n  - template: Security/SAST.gitlab-ci.yml' > .gitlab-ci.yml"}
        ]
    },
    40: {
        "name": "☁️ Cloud CLI Mastery",
        "description": "Manage cloud resources from command line",
        "what_you_learn": "AWS CLI, GCP gcloud, Azure CLI commands",
        "objective": "Master cloud CLI tools",
        "category": "Expert",
        "difficulty": 9,
        "hint": "aws, gcloud, az commands",
        "flag": "CTF{cloud_cli_master}",
        "tasks": [
            {"instruction": "Install AWS CLI", "check": "pip install awscli"},
            {"instruction": "Configure AWS CLI", "check": "aws configure"},
            {"instruction": "List EC2 instances", "check": "aws ec2 describe-instances"},
            {"instruction": "Create S3 bucket", "check": "aws s3 mb s3://my-unique-bucket-2024"},
            {"instruction": "List S3 buckets", "check": "aws s3 ls"},
            {"instruction": "Sync to S3", "check": "aws s3 sync /local/dir s3://my-bucket/"},
            {"instruction": "Install GCP gcloud", "check": "curl https://sdk.cloud.google.com | bash"},
            {"instruction": "Authenticate to GCP", "check": "gcloud auth login"},
            {"instruction": "List GCP instances", "check": "gcloud compute instances list"},
            {"instruction": "Create GCP VM", "check": "gcloud compute instances create my-vm --zone=us-central1-a"},
            {"instruction": "Install Azure CLI", "check": "curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash"},
            {"instruction": "Login to Azure", "check": "az login"},
            {"instruction": "List Azure VMs", "check": "az vm list"},
            {"instruction": "Create Azure VM", "check": "az vm create --name my-vm --resource-group my-rg --image UbuntuLTS"}
        ]
    },
    41: {
        "name": "🏗️ Infrastructure as Code",
        "description": "Manage infrastructure with code",
        "what_you_learn": "Terraform, Ansible, CloudFormation basics",
        "objective": "Master IaC tools",
        "category": "Master",
        "difficulty": 9,
        "hint": "terraform, ansible, cloudformation",
        "flag": "CTF{iac_master_2024}",
        "tasks": [
            {"instruction": "Install Terraform", "check": "wget https://releases.hashicorp.com/terraform/1.5.0/terraform_1.5.0_linux_amd64.zip"},
            {"instruction": "Initialize Terraform", "check": "terraform init"},
            {"instruction": "Create Terraform plan", "check": "echo 'provider \"aws\" { region = \"us-east-1\" }\\nresource \"aws_instance\" \"web\" { ami = \"ami-12345678\" instance_type = \"t2.micro\" }' > main.tf"},
            {"instruction": "Plan Terraform changes", "check": "terraform plan"},
            {"instruction": "Apply Terraform changes", "check": "terraform apply -auto-approve"},
            {"instruction": "Destroy Terraform resources", "check": "terraform destroy -auto-approve"},
            {"instruction": "Install Ansible", "check": "apt install ansible"},
            {"instruction": "Create Ansible inventory", "check": "echo '[webservers]\\n192.168.1.10\\n192.168.1.11' > inventory.ini"},
            {"instruction": "Create Ansible playbook", "check": "echo '- hosts: webservers\\n  tasks:\\n    - name: Install nginx\\n      apt: name=nginx state=present' > playbook.yml"},
            {"instruction": "Run Ansible playbook", "check": "ansible-playbook -i inventory.ini playbook.yml"},
            {"instruction": "Test Ansible connection", "check": "ansible all -i inventory.ini -m ping"},
            {"instruction": "Create AWS CloudFormation", "check": "echo '{\"Resources\": {\"MyEC2Instance\": {\"Type\": \"AWS::EC2::Instance\", \"Properties\": {\"ImageId\": \"ami-12345678\"}}}}' > template.json"},
            {"instruction": "Create CloudFormation stack", "check": "aws cloudformation create-stack --stack-name my-stack --template-body file://template.json"},
            {"instruction": "Delete CloudFormation stack", "check": "aws cloudformation delete-stack --stack-name my-stack"}
        ]
    },
    42: {
        "name": "📊 Monitoring & Alerting",
        "description": "Set up monitoring and alerting systems",
        "what_you_learn": "Prometheus, Grafana, Nagios, Alertmanager",
        "objective": "Master monitoring and alerting",
        "category": "Master",
        "difficulty": 8,
        "hint": "prometheus, grafana, nagios, alerts",
        "flag": "CTF{monitoring_master}",
        "tasks": [
            {"instruction": "Download Prometheus", "check": "wget https://github.com/prometheus/prometheus/releases/latest/download/prometheus-2.40.0.linux-amd64.tar.gz"},
            {"instruction": "Extract Prometheus", "check": "tar -xzf prometheus-2.40.0.linux-amd64.tar.gz"},
            {"instruction": "Start Prometheus", "check": "./prometheus --config.file=prometheus.yml &"},
            {"instruction": "Check Prometheus status", "check": "curl http://localhost:9090/status"},
            {"instruction": "Install Grafana", "check": "wget https://dl.grafana.com/oss/release/grafana_9.0.0_amd64.deb"},
            {"instruction": "Start Grafana", "check": "systemctl start grafana-server"},
            {"instruction": "Check Grafana status", "check": "systemctl status grafana-server"},
            {"instruction": "Add Prometheus data source", "check": "curl -X POST http://localhost:3000/api/datasources -H 'Content-Type: application/json' -d '{\"name\":\"Prometheus\",\"type\":\"prometheus\",\"url\":\"http://localhost:9090\"}'"},
            {"instruction": "Install Nagios", "check": "apt install nagios4"},
            {"instruction": "Create Nagios check", "check": "echo 'check_command check_http' >> /etc/nagios/nrpe.cfg"},
            {"instruction": "Install Alertmanager", "check": "wget https://github.com/prometheus/alertmanager/releases/latest/download/alertmanager-0.24.0.linux-amd64.tar.gz"},
            {"instruction": "Create alert rule", "check": "echo 'groups:\\n- name: example\\n  rules:\\n  - alert: HighCPU\\n    expr: cpu_usage > 80' > alert.rules"},
            {"instruction": "Configure Grafana dashboard", "check": "grafana-cli plugins install grafana-piechart-panel"},
            {"instruction": "Set up Slack alerts", "check": "echo 'slack_configs:\\n  - api_url: https://hooks.slack.com/services/...' >> alertmanager.yml"}
        ]
    },
    43: {
        "name": "📝 Logging & ELK Stack",
        "description": "Centralized logging with ELK Stack",
        "what_you_learn": "Elasticsearch, Logstash, Kibana, Filebeat",
        "objective": "Master ELK Stack for logging",
        "category": "Master",
        "difficulty": 9,
        "hint": "elasticsearch, logstash, kibana, filebeat",
        "flag": "CTF{elk_master_2024}",
        "tasks": [
            {"instruction": "Install Elasticsearch", "check": "wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -"},
            {"instruction": "Start Elasticsearch", "check": "systemctl start elasticsearch"},
            {"instruction": "Check Elasticsearch status", "check": "curl -X GET 'localhost:9200'"},
            {"instruction": "Install Kibana", "check": "apt install kibana"},
            {"instruction": "Start Kibana", "check": "systemctl start kibana"},
            {"instruction": "Install Logstash", "check": "apt install logstash"},
            {"instruction": "Create Logstash pipeline", "check": "echo 'input { beats { port => 5044 } } output { elasticsearch { hosts => [\"localhost:9200\"] } }' > /etc/logstash/conf.d/beats.conf"},
            {"instruction": "Start Logstash", "check": "systemctl start logstash"},
            {"instruction": "Install Filebeat", "check": "apt install filebeat"},
            {"instruction": "Configure Filebeat", "check": "echo 'filebeat.inputs:\\n- type: log\\n  enabled: true\\n  paths:\\n    - /var/log/*.log' > /etc/filebeat/filebeat.yml"},
            {"instruction": "Start Filebeat", "check": "systemctl start filebeat"},
            {"instruction": "Create Elasticsearch index", "check": "curl -X PUT 'localhost:9200/my-index'"},
            {"instruction": "Query Elasticsearch", "check": "curl -X GET 'localhost:9200/_search?q=*'"},
            {"instruction": "Create Kibana dashboard", "check": "curl -X POST 'localhost:5601/api/saved_objects/dashboard' -H 'kbn-xsrf: true' -d '{\"attributes\":{\"title\":\"My Dashboard\"}}'"}
        ]
    },
    44: {
        "name": "🛡️ Security Hardening",
        "description": "Harden Linux system security",
        "what_you_learn": "Security best practices, auditing, SELinux, AppArmor",
        "objective": "Master system security hardening",
        "category": "Master",
        "difficulty": 9,
        "hint": "auditd, SELinux, AppArmor, fail2ban",
        "flag": "CTF{security_hardened_2024}",
        "tasks": [
            {"instruction": "Enable SELinux", "check": "setenforce 1"},
            {"instruction": "Check SELinux status", "check": "getenforce"},
            {"instruction": "Install AppArmor", "check": "apt install apparmor"},
            {"instruction": "Enable AppArmor", "check": "aa-enforce /usr/sbin/nginx"},
            {"instruction": "Install fail2ban", "check": "apt install fail2ban"},
            {"instruction": "Start fail2ban", "check": "systemctl start fail2ban"},
            {"instruction": "Configure fail2ban for SSH", "check": "echo '[sshd]\\nenabled = true\\nport = ssh\\nfilter = sshd\\nlogpath = /var/log/auth.log\\nmaxretry = 3' > /etc/fail2ban/jail.local"},
            {"instruction": "Install auditd", "check": "apt install auditd"},
            {"instruction": "Create audit rule", "check": "auditctl -w /etc/passwd -p wa -k identity"},
            {"instruction": "List audit rules", "check": "auditctl -l"},
            {"instruction": "Check failed login attempts", "check": "grep 'Failed password' /var/log/auth.log"},
            {"instruction": "Configure password policy", "check": "chage -M 90 -m 7 -W 7 user"},
            {"instruction": "Disable unused services", "check": "systemctl disable bluetooth"},
            {"instruction": "Set up security updates", "check": "echo 'APT::Periodic::Update-Package-Lists \"1\";' >> /etc/apt/apt.conf.d/20auto-upgrades"}
        ]
    },
    45: {
        "name": "⚡ Performance Tuning",
        "description": "Optimize system performance",
        "what_you_learn": "Kernel tuning, sysctl, performance analysis",
        "objective": "Master system performance tuning",
        "category": "Master",
        "difficulty": 10,
        "hint": "sysctl, kernel parameters, performance tools",
        "flag": "CTF{performance_tuner}",
        "tasks": [
            {"instruction": "Show all sysctl parameters", "check": "sysctl -a"},
            {"instruction": "Optimize TCP parameters", "check": "sysctl -w net.ipv4.tcp_syncookies=1"},
            {"instruction": "Increase file descriptors", "check": "sysctl -w fs.file-max=1000000"},
            {"instruction": "Optimize swappiness", "check": "sysctl -w vm.swappiness=10"},
            {"instruction": "Increase TCP buffer", "check": "sysctl -w net.core.rmem_max=16777216"},
            {"instruction": "Optimize TCP congestion", "check": "sysctl -w net.ipv4.tcp_congestion_control=bbr"},
            {"instruction": "Show CPU performance", "check": "cpupower frequency-info"},
            {"instruction": "Set CPU governor", "check": "cpupower frequency-set -g performance"},
            {"instruction": "Check I/O scheduler", "check": "cat /sys/block/sda/queue/scheduler"},
            {"instruction": "Set I/O scheduler", "check": "echo deadline > /sys/block/sda/queue/scheduler"},
            {"instruction": "Analyze system with perf", "check": "perf stat -e cycles,instructions ls"},
            {"instruction": "Use strace for debugging", "check": "strace -c ls"},
            {"instruction": "Check process limits", "check": "ulimit -a"},
            {"instruction": "Optimize kernel parameters", "check": "echo 'net.core.somaxconn=1024' >> /etc/sysctl.conf"}
        ]
    },
    46: {
        "name": "🌐 Advanced Networking",
        "description": "Advanced network configuration",
        "what_you_learn": "VLANs, bonding, bridging, routing, network namespaces",
        "objective": "Master advanced networking",
        "category": "Master",
        "difficulty": 10,
        "hint": "vlan, bond, bridge, network namespaces",
        "flag": "CTF{network_expert_2024}",
        "tasks": [
            {"instruction": "Create VLAN interface", "check": "ip link add link eth0 name eth0.100 type vlan id 100"},
            {"instruction": "Create bond interface", "check": "ip link add bond0 type bond mode 802.3ad"},
            {"instruction": "Add interfaces to bond", "check": "ip link set eth1 master bond0"},
            {"instruction": "Create bridge interface", "check": "brctl addbr br0"},
            {"instruction": "Add interface to bridge", "check": "brctl addif br0 eth0"},
            {"instruction": "Create network namespace", "check": "ip netns add myns"},
            {"instruction": "List network namespaces", "check": "ip netns list"},
            {"instruction": "Execute command in namespace", "check": "ip netns exec myns ip addr"},
            {"instruction": "Create veth pair", "check": "ip link add veth0 type veth peer name veth1"},
            {"instruction": "Move veth to namespace", "check": "ip link set veth1 netns myns"},
            {"instruction": "Configure BGP routing", "check": "bird -c bird.conf"},
            {"instruction": "Setup policy routing", "check": "ip rule add from 192.168.1.0/24 table 100"},
            {"instruction": "Create network policy", "check": "echo 'nft add rule inet filter input drop'"},
            {"instruction": "Configure QoS", "check": "tc qdisc add dev eth0 root handle 1: htb default 30"}
        ]
    },
    47: {
        "name": "🖥️ Virtualization",
        "description": "Manage virtual machines with KVM/QEMU",
        "what_you_learn": "KVM, QEMU, libvirt, virsh commands",
        "objective": "Master virtualization",
        "category": "Master",
        "difficulty": 10,
        "hint": "virsh, virt-install, qemu, libvirt",
        "flag": "CTF{virt_master_2024}",
        "tasks": [
            {"instruction": "Check KVM support", "check": "kvm-ok"},
            {"instruction": "Install KVM packages", "check": "apt install qemu-kvm libvirt-daemon-system"},
            {"instruction": "Start libvirtd service", "check": "systemctl start libvirtd"},
            {"instruction": "Check libvirtd status", "check": "systemctl status libvirtd"},
            {"instruction": "List virtual networks", "check": "virsh net-list"},
            {"instruction": "Create VM with virt-install", "check": "virt-install --name vm1 --memory 2048 --vcpus 2 --disk size=10 --cdrom ubuntu.iso"},
            {"instruction": "List all VMs", "check": "virsh list --all"},
            {"instruction": "Start VM", "check": "virsh start vm1"},
            {"instruction": "Stop VM", "check": "virsh shutdown vm1"},
            {"instruction": "Delete VM", "check": "virsh destroy vm1 && virsh undefine vm1"},
            {"instruction": "Create VM snapshot", "check": "virsh snapshot-create-as vm1 snap1"},
            {"instruction": "List VM snapshots", "check": "virsh snapshot-list vm1"},
            {"instruction": "Connect to VM console", "check": "virsh console vm1"},
            {"instruction": "Show VM info", "check": "virsh dominfo vm1"}
        ]
    },
    48: {
        "name": "🤖 Automation Master",
        "description": "Infrastructure automation",
        "what_you_learn": "Ansible, Puppet, Chef, configuration management",
        "objective": "Master automation tools",
        "category": "Master",
        "difficulty": 10,
        "hint": "ansible-playbook, puppet apply, chef-solo",
        "flag": "CTF{automation_master}",
        "tasks": [
            {"instruction": "Install Ansible", "check": "apt install ansible"},
            {"instruction": "Create Ansible inventory", "check": "echo '[webservers]\\nweb1 ansible_host=192.168.1.10\\nweb2 ansible_host=192.168.1.11' > inventory.ini"},
            {"instruction": "Create Ansible playbook", "check": "echo '---\\n- hosts: webservers\\n  become: yes\\n  tasks:\\n    - name: Install nginx\\n      apt: name=nginx state=present\\n    - name: Start nginx\\n      service: name=nginx state=started' > playbook.yml"},
            {"instruction": "Run Ansible playbook", "check": "ansible-playbook -i inventory.ini playbook.yml"},
            {"instruction": "Install Puppet", "check": "apt install puppet"},
            {"instruction": "Create Puppet manifest", "check": "echo 'package { \"nginx\": ensure => installed }' > manifest.pp"},
            {"instruction": "Apply Puppet manifest", "check": "puppet apply manifest.pp"},
            {"instruction": "Install Chef", "check": "curl -L https://omnitruck.chef.io/install.sh | bash"},
            {"instruction": "Create Chef recipe", "check": "echo 'package \"nginx\"' > recipe.rb"},
            {"instruction": "Run Chef recipe", "check": "chef-solo -o recipe.rb"},
            {"instruction": "Create Ansible role", "check": "ansible-galaxy init webserver"},
            {"instruction": "Use Ansible vault", "check": "ansible-vault encrypt secrets.yml"},
            {"instruction": "List Ansible modules", "check": "ansible-doc -l"},
            {"instruction": "Create Ansible dynamic inventory", "check": "ansible-inventory -i aws_ec2.yml --list"}
        ]
    },
    49: {
        "name": "🔄 High Availability",
        "description": "Configure high availability systems",
        "what_you_learn": "Pacemaker, Corosync, HAProxy, load balancing",
        "objective": "Master high availability",
        "category": "Master",
        "difficulty": 10,
        "hint": "pacemaker, corosync, haproxy, keepalived",
        "flag": "CTF{ha_master_2024}",
        "tasks": [
            {"instruction": "Install HAProxy", "check": "apt install haproxy"},
            {"instruction": "Configure HAProxy", "check": "echo 'frontend http-in\\n    bind *:80\\n    default_backend servers\\nbackend servers\\n    server server1 192.168.1.10:80 check\\n    server server2 192.168.1.11:80 check' > /etc/haproxy/haproxy.cfg"},
            {"instruction": "Start HAProxy", "check": "systemctl start haproxy"},
            {"instruction": "Install Keepalived", "check": "apt install keepalived"},
            {"instruction": "Configure Keepalived", "check": "echo 'vrrp_instance VI_1 {\\n    state MASTER\\n    interface eth0\\n    virtual_router_id 51\\n    priority 100\\n    advert_int 1\\n    authentication {\\n        auth_type PASS\\n        auth_pass 1234\\n    }\\n    virtual_ipaddress {\\n        192.168.1.100\\n    }\\n}' > /etc/keepalived/keepalived.conf"},
            {"instruction": "Start Keepalived", "check": "systemctl start keepalived"},
            {"instruction": "Install Pacemaker", "check": "apt install pacemaker"},
            {"instruction": "Start Pacemaker", "check": "systemctl start pacemaker"},
            {"instruction": "Configure Corosync", "check": "echo 'service {\\n    name: pacemaker\\n    ver: 0\\n}\\naisexec {\\n    user: root\\n    group: root\\n}' > /etc/corosync/corosync.conf"},
            {"instruction": "Create cluster resource", "check": "pcs resource create VIP ocf:heartbeat:IPaddr2 ip=192.168.1.200 cidr_netmask=24"},
            {"instruction": "Add cluster constraint", "check": "pcs constraint colocation add VIP with nginx"},
            {"instruction": "Set up DRBD", "check": "drbdadm create-md res0"},
            {"instruction": "Check cluster status", "check": "pcs status"},
            {"instruction": "Configure load balancer", "check": "echo 'listen stats\\n    bind *:1936\\n    stats enable' >> /etc/haproxy/haproxy.cfg"}
        ]
    },
    50: {
        "name": "🏆 Ultimate Linux Master",
        "description": "The final challenge - everything combined",
        "what_you_learn": "All Linux skills combined - the ultimate test",
        "objective": "Complete the ultimate Linux mastery challenge",
        "category": "Master",
        "difficulty": 10,
        "hint": "Use every skill you've learned!",
        "flag": "CTF{ultimate_linux_master_2024}",
        "tasks": [
            {"instruction": "Check system information", "check": "uname -a && lscpu && free -h && df -h"},
            {"instruction": "Check network configuration", "check": "ip addr && ip route && ss -tuln"},
            {"instruction": "Check running services", "check": "systemctl list-units --type=service --state=running"},
            {"instruction": "Find all files modified in last 24 hours", "check": "find / -mtime -1 -type f 2>/dev/null | head -20"},
            {"instruction": "Check system logs for errors", "check": "grep -r ERROR /var/log/ 2>/dev/null | head -20"},
            {"instruction": "Create and run a bash script", "check": "echo '#!/bin/bash' > master.sh && echo 'echo \"Linux Master\"' >> master.sh && chmod +x master.sh && ./master.sh"},
            {"instruction": "Check process status", "check": "ps aux --sort=-%mem | head -10"},
            {"instruction": "Check disk usage", "check": "du -sh /* 2>/dev/null | sort -hr | head -10"},
            {"instruction": "Check network connections", "check": "netstat -tunap | grep ESTABLISHED"},
            {"instruction": "Check system load", "check": "uptime && top -bn1 | head -10"},
            {"instruction": "Check security status", "check": "getenforce && systemctl status fail2ban"},
            {"instruction": "Check docker containers", "check": "docker ps -a 2>/dev/null || echo \"Docker not found\""},
            {"instruction": "Check Kubernetes pods", "check": "kubectl get pods --all-namespaces 2>/dev/null || echo \"Kubernetes not found\""},
            {"instruction": "Check cloud resources", "check": "aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,State.Name]' 2>/dev/null || echo \"AWS CLI not configured\""},
            {"instruction": "Create backup", "check": "tar -czf /tmp/backup_$(date +%Y%m%d).tar.gz /etc/hostname 2>/dev/null"},
            {"instruction": "Check system performance", "check": "vmstat 1 5 && iostat -x 1 3"},
            {"instruction": "Check network performance", "check": "ping -c 4 google.com"},
            {"instruction": "Find the final flag", "check": "echo 'CTF{ultimate_linux_master_2024}' && echo '🐧 You are now a Linux Master!'"}
        ]
    }
}

# ============================================
# ACHIEVEMENTS
# ============================================

ACHIEVEMENTS = {
    "first_steps": {"name": "First Steps", "desc": "Complete Level 1", "icon": "🌟"},
    "beginner_5": {"name": "Quick Learner", "desc": "Complete 5 levels", "icon": "📚"},
    "beginner_10": {"name": "Beginner Graduate", "desc": "Complete 10 levels", "icon": "🎓"},
    "intermediate_15": {"name": "Rising Star", "desc": "Complete 15 levels", "icon": "⭐"},
    "intermediate_20": {"name": "Intermediate Expert", "desc": "Complete 20 levels", "icon": "🏅"},
    "expert_30": {"name": "Expert Level", "desc": "Complete 30 levels", "icon": "🔥"},
    "master_40": {"name": "Power User", "desc": "Complete 40 levels", "icon": "👑"},
    "master_50": {"name": "Ultimate Legend", "desc": "Complete all 50 levels", "icon": "🏆"},
    "speed_demon": {"name": "Speed Demon", "desc": "Complete 10 levels under 2 minutes", "icon": "⚡"},
    "perfect_run": {"name": "Perfect Run", "desc": "Complete 10 levels with no hints", "icon": "💯"},
    "streak_master": {"name": "Streak Master", "desc": "Get 20 correct answers in a row", "icon": "🔥"},
    "hint_avoider": {"name": "Hint Avoider", "desc": "Complete 20 levels without hints", "icon": "🚫"},
    "persistent": {"name": "Persistent", "desc": "Play for 10+ hours total", "icon": "💪"},
    "perfect_accuracy": {"name": "Perfect Accuracy", "desc": "Achieve 95% accuracy overall", "icon": "🎯"},
    "linux_guru": {"name": "Linux Guru", "desc": "Complete all 50 levels with 90%+ accuracy", "icon": "🐧"}
}

# ============================================
# COMMAND REFERENCE
# ============================================

COMMAND_REFERENCE = {
    "ls": {"usage": "ls [options] [directory]", "description": "List directory contents", "options": {"-l": "Long format", "-a": "Show hidden files", "-h": "Human-readable"}, "examples": ["ls -la", "ls -ltr"]},
    "cd": {"usage": "cd [directory]", "description": "Change directory", "options": {"~": "Home", "..": "Parent", "-": "Previous"}, "examples": ["cd /home", "cd .."]},
    "pwd": {"usage": "pwd", "description": "Print working directory", "options": {}, "examples": ["pwd"]},
    "mkdir": {"usage": "mkdir [options] directory", "description": "Create directory", "options": {"-p": "Create parents"}, "examples": ["mkdir test", "mkdir -p a/b/c"]},
    "rm": {"usage": "rm [options] file", "description": "Remove files", "options": {"-r": "Recursive", "-f": "Force", "-i": "Interactive"}, "examples": ["rm file.txt", "rm -rf folder"]},
    "cp": {"usage": "cp [options] source dest", "description": "Copy files", "options": {"-r": "Recursive", "-p": "Preserve", "-i": "Interactive"}, "examples": ["cp file1 file2", "cp -r dir1 dir2"]},
    "mv": {"usage": "mv [options] source dest", "description": "Move/rename files", "options": {"-i": "Interactive", "-f": "Force", "-u": "Update"}, "examples": ["mv file1 file2", "mv file dir/"]},
    "grep": {"usage": "grep [options] pattern [files]", "description": "Search for patterns", "options": {"-r": "Recursive", "-i": "Case insensitive", "-n": "Line numbers", "-w": "Whole word"}, "examples": ["grep error log.txt", "grep -r TODO ."]},
    "find": {"usage": "find [path] [options]", "description": "Search for files", "options": {"-name": "By name", "-type": "By type", "-size": "By size", "-mtime": "By modification"}, "examples": ["find . -name '*.txt'", "find / -size +10M"]},
    "chmod": {"usage": "chmod [options] mode file", "description": "Change permissions", "options": {"u+x": "Add execute", "755": "rwx r-x r-x", "644": "rw- r-- r--"}, "examples": ["chmod +x script.sh", "chmod 755 file.txt"]},
    "ps": {"usage": "ps [options]", "description": "Process status", "options": {"aux": "All processes", "ef": "Full format"}, "examples": ["ps aux", "ps aux --sort=-%cpu"]},
    "top": {"usage": "top [options]", "description": "Real-time monitoring", "options": {"-u": "User", "-p": "PID"}, "examples": ["top", "top -u user"]},
    "kill": {"usage": "kill [options] PID", "description": "Send signals", "options": {"-9": "Force kill", "-15": "Terminate", "-STOP": "Pause"}, "examples": ["kill 1234", "kill -9 1234"]}
}

# ============================================
# GAME ENGINE
# ============================================

class CTFGame:
    def __init__(self):
        self.username = ""
        self.current_level = 1
        self.score = 0
        self.xp = 0
        self.hints_used = 0
        self.completed_levels = []
        self.achievements = []
        self.streak = 0
        self.max_streak = 0
        self.total_attempts = 0
        self.correct_attempts = 0
        self.level_stats = {}
        self.command_history = []
        self.running = True
        self.game_mode = "normal"
        self.total_play_time = 0
        self.start_time = time.time()
        self.level_start_time = None

    def load_game(self):
        save_file = os.path.expanduser("~/.linux_ctf_50.json")
        if os.path.exists(save_file):
            try:
                with open(save_file, 'r') as f:
                    data = json.load(f)
                    for key in ['username', 'current_level', 'score', 'xp', 'hints_used',
                               'completed_levels', 'achievements', 'streak', 'max_streak',
                               'total_attempts', 'correct_attempts', 'level_stats', 'total_play_time']:
                        if key in data:
                            setattr(self, key, data[key])
                return True
            except:
                pass
        return False

    def save_game(self):
        save_file = os.path.expanduser("~/.linux_ctf_50.json")
        data = {
            'username': self.username,
            'current_level': self.current_level,
            'score': self.score,
            'xp': self.xp,
            'hints_used': self.hints_used,
            'completed_levels': self.completed_levels,
            'achievements': self.achievements,
            'streak': self.streak,
            'max_streak': self.max_streak,
            'total_attempts': self.total_attempts,
            'correct_attempts': self.correct_attempts,
            'level_stats': self.level_stats,
            'total_play_time': self.total_play_time
        }
        try:
            with open(save_file, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except:
            return False

    def clear_screen(self):
        os.system('clear' if os.name != 'nt' else 'cls')

    def print_colored(self, text, color=Colors.WHITE, bold=False):
        if bold:
            print(f"{color}{Colors.BOLD}{text}{Colors.RESET}")
        else:
            print(f"{color}{text}{Colors.RESET}")

    def print_header(self):
        print("=" * 85)
        self.print_colored("        🏴 LEARN WITH N4MR3S", Colors.CYAN, True)
        print("=" * 85)
        if self.username:
            print(f"👤 {Colors.BOLD}{self.username}{Colors.RESET}  |  "
                  f"🏆 Score: {Colors.YELLOW}{self.score}{Colors.RESET}  |  "
                  f"⭐ XP: {Colors.BLUE}{self.xp}{Colors.RESET}  |  "
                  f"📍 Level: {Colors.BOLD}{self.current_level}/50{Colors.RESET}")
            print(f"🔥 Streak: {Colors.RED}{self.streak}{Colors.RESET}  |  "
                  f"🏅 Achievements: {len(self.achievements)}/{len(ACHIEVEMENTS)}  |  "
                  f"📊 Accuracy: {self.get_accuracy()}%")
        print("-" * 85)

    def get_play_time(self):
        total_seconds = self.total_play_time + (time.time() - self.start_time)
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        if hours > 0:
            return f"{hours}h {minutes}m"
        return f"{minutes}m"

    def get_accuracy(self):
        if self.total_attempts == 0:
            return 100
        return int((self.correct_attempts / self.total_attempts) * 100)

    def print_level_info(self, level_num):
        if level_num not in LEVELS:
            return
        level = LEVELS[level_num]
        category_colors = {
            "Beginner": Colors.GREEN,
            "Intermediate": Colors.YELLOW,
            "Advanced": Colors.CYAN,
            "Expert": Colors.MAGENTA,
            "Master": Colors.RED
        }
        color = category_colors.get(level.get('category', 'Beginner'), Colors.WHITE)

        print(f"\n📚 {Colors.BOLD}LEVEL {level_num}/50{Colors.RESET}: {level['name']}")
        print("-" * 85)
        print(f"📝 {level['description']}")
        print(f"🎯 {level['objective']}")
        print(f"📖 {Colors.CYAN}What you'll learn:{Colors.RESET} {level['what_you_learn']}")
        print(f"📊 Category: {color}{level.get('category', 'Beginner')}{Colors.RESET}  |  Difficulty: {'⭐' * level.get('difficulty', 1)}")
        print(f"💡 Type '{Colors.CYAN}help{Colors.RESET}' for commands")
        print("-" * 85)

    def validate_command(self, command, task_check):
        # A task must match the complete expected command.
        # Do not accept a command merely because its base command
        # appears inside the expected command (e.g. `cd ` must not
        # pass a task whose answer is `cd -`).
        return command.strip() == task_check.strip()

    def simulate_command(self, command):
        print(f"\n💻 {Colors.CYAN}Command executed:{Colors.RESET}")
        print(f"$ {Colors.YELLOW}{command}{Colors.RESET}")
        print("-" * 50)
        if 'ls' in command:
            print("file1.txt  file2.txt  notes.txt  .hidden_file  projects/")
        elif 'pwd' in command:
            print("/home/user/current_directory")
        elif 'cd' in command:
            print("📁 Directory changed")
        elif 'mkdir' in command:
            print("✅ Directory created")
        elif 'touch' in command or 'echo' in command:
            print("✅ File operation completed")
        elif 'cat' in command or 'head' in command or 'tail' in command:
            print("File contents displayed")
        elif 'cp' in command:
            print("✅ File copied")
        elif 'mv' in command:
            print("✅ File moved/renamed")
        elif 'rm' in command:
            print("✅ File removed")
        elif 'grep' in command or 'find' in command:
            print("Search results found")
        elif 'chmod' in command or 'chown' in command:
            print("✅ Permissions changed")
        elif 'ln' in command:
            print("✅ Link created")
        elif 'ps' in command or 'top' in command:
            print("Process list displayed")
        elif 'kill' in command:
            print("✅ Process terminated")
        elif 'ping' in command:
            print("PING google.com (172.217.0.46) - 64 bytes from...")
        elif 'ss' in command or 'netstat' in command:
            print("Network connections displayed")
        elif 'ip' in command:
            print("Network interfaces displayed")
        elif 'uname' in command or 'free' in command or 'df' in command:
            print("System information displayed")
        elif 'systemctl' in command:
            print("✅ Service management completed")
        elif 'docker' in command:
            print("🐳 Docker command executed")
        elif 'kubectl' in command:
            print("☸️ Kubernetes command executed")
        elif 'aws' in command or 'gcloud' in command or 'az' in command:
            print("☁️ Cloud CLI command executed")
        else:
            print("✅ Command accepted")
        print("-" * 50)

    def check_achievements(self):
        new_achievements = []
        completed = len(self.completed_levels)

        if 1 in self.completed_levels and "first_steps" not in self.achievements:
            new_achievements.append("first_steps")
        if completed >= 5 and "beginner_5" not in self.achievements:
            new_achievements.append("beginner_5")
        if completed >= 10 and "beginner_10" not in self.achievements:
            new_achievements.append("beginner_10")
        if completed >= 15 and "intermediate_15" not in self.achievements:
            new_achievements.append("intermediate_15")
        if completed >= 20 and "intermediate_20" not in self.achievements:
            new_achievements.append("intermediate_20")
        if completed >= 30 and "expert_30" not in self.achievements:
            new_achievements.append("expert_30")
        if completed >= 40 and "master_40" not in self.achievements:
            new_achievements.append("master_40")
        if completed >= 50 and "master_50" not in self.achievements:
            new_achievements.append("master_50")
        if self.max_streak >= 20 and "streak_master" not in self.achievements:
            new_achievements.append("streak_master")
        if self.get_accuracy() >= 95 and "perfect_accuracy" not in self.achievements:
            new_achievements.append("perfect_accuracy")
        if completed >= 50 and self.get_accuracy() >= 90 and "linux_guru" not in self.achievements:
            new_achievements.append("linux_guru")

        for ach in new_achievements:
            if ach not in self.achievements:
                self.achievements.append(ach)
                if ach in ACHIEVEMENTS:
                    a = ACHIEVEMENTS[ach]
                    self.print_colored(f"\n🎉 ACHIEVEMENT UNLOCKED: {a['icon']} {a['name']}", Colors.MAGENTA, True)
                    print(f"   {a['desc']}")
                    self.xp += 50
                    time.sleep(0.5)
        if new_achievements:
            self.save_game()

    def show_command_reference(self, command_name=None):
        self.clear_screen()
        self.print_header()
        if command_name and command_name in COMMAND_REFERENCE:
            cmd = COMMAND_REFERENCE[command_name]
            self.print_colored(f"\n📚 Command: {command_name}", Colors.CYAN, True)
            print("-" * 50)
            print(f"Usage: {cmd['usage']}")
            print(f"Description: {cmd['description']}")
            if cmd['options']:
                print("\nOptions:")
                for opt, desc in cmd['options'].items():
                    print(f"  {opt:10} {desc}")
            if cmd['examples']:
                print("\nExamples:")
                for ex in cmd['examples']:
                    print(f"  {ex}")
        else:
            self.print_colored("\n📚 Available Commands:", Colors.CYAN, True)
            print("-" * 50)
            cmds = sorted(COMMAND_REFERENCE.keys())
            for i, cmd in enumerate(cmds, 1):
                print(f"{i:3}. {cmd}")
            print("\nType: 'ref <command>' for detailed info")
        input("\nPress Enter to continue...")

    def play_level(self, level_num):
        if level_num not in LEVELS:
            return False

        level = LEVELS[level_num]
        self.level_start_time = time.time()
        level_hints = 0

        for task in level['tasks']:
            task['completed'] = False

        while self.running:
            self.clear_screen()
            self.print_header()
            self.print_level_info(level_num)

            completed = sum(1 for task in level['tasks'] if task.get('completed', False))
            total = len(level['tasks'])
            progress_bar = "█" * completed + "░" * (total - completed)
            print(f"\n📊 Progress: {progress_bar} {completed}/{total}")

            if self.game_mode == "time_attack":
                elapsed = int(time.time() - self.level_start_time)
                print(f"⏱️  Time: {elapsed}s (Target: <120s)")

            if completed == total:
                time_taken = time.time() - self.level_start_time
                self.total_play_time += time_taken

                self.clear_screen()
                self.print_header()
                self.print_colored(f"\n🎉 LEVEL {level_num}/50 COMPLETE!", Colors.GREEN, True)
                self.print_colored(f"🏆 Flag: {level['flag']}", Colors.YELLOW, True)
                print(f"⏱️  Time: {int(time_taken)} seconds")
                print(f"💡 Hints used: {level_hints}")
                print(f"📖 Learned: {level['what_you_learn']}")

                bonus = 0
                time_bonus = 0

                if self.game_mode == "time_attack" and time_taken < 120:
                    time_bonus = 30
                    self.print_colored("⚡ Time Attack Bonus! +30 XP", Colors.CYAN)
                elif time_taken < 120:
                    time_bonus = 20
                    self.print_colored("⚡ Speed bonus! +20 XP", Colors.CYAN)
                elif time_taken < 180:
                    time_bonus = 10
                    self.print_colored("⚡ Good speed! +10 XP", Colors.CYAN)

                if level_hints == 0:
                    bonus += 15
                    self.print_colored("💯 Perfect run! +15 XP", Colors.MAGENTA)

                points = 50 + bonus + time_bonus
                xp_gain = 30 + bonus + time_bonus
                self.score += points
                self.xp += xp_gain
                self.completed_levels.append(level_num)
                self.level_stats[level_num] = {
                    'completed': True,
                    'time': time_taken,
                    'hints_used': level_hints,
                    'score': points,
                    'mode': self.game_mode
                }
                self.current_level = level_num + 1
                self.save_game()

                print(f"\n✨ +{points} points! | +{xp_gain} XP!")
                self.check_achievements()

                if level_num + 1 <= len(LEVELS):
                    next_level = LEVELS[level_num + 1]
                    print(f"\n📚 Next Level Preview:")
                    print(f"   {next_level['name']}")
                    print(f"   {Colors.DIM}What you'll learn: {next_level['what_you_learn']}{Colors.RESET}")

                input("\nPress Enter to continue...")
                return True

            current_task = None
            for task in level['tasks']:
                if not task.get('completed', False):
                    current_task = task
                    break

            if current_task:
                print(f"\n{Colors.BOLD}{Colors.YELLOW}⚠️ ATTENTION — LEARN BY DOING{Colors.RESET}")
                print("-" * 78)
                print("💻 Open another terminal alongside this game.")
                print("👉 Try the commands you are learning in that terminal and observe")
                print("   what they actually do.")
                print("💡 Experiment with command options/flags and observe the output.")
                print("   The goal is to understand the command, not just memorize it.")
                print("-" * 78)
                print(f"\n📌 {Colors.BOLD}Task:{Colors.RESET} {current_task['instruction']}")
                print(f"💡 {Colors.DIM}Expected: {current_task['check']}{Colors.RESET}")
                print("-" * 50)

                user_input = input(f"{Colors.GREEN}💻 ${Colors.RESET} ").strip()

                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("\n👋 Thanks for playing!")
                    self.running = False
                    return False

                elif user_input.lower() == 'help':
                    print("\n📚 {Colors.BOLD}Available commands:{Colors.RESET}")
                    print("  <linux command>     - Try to solve the task")
                    print("  hint                - Show a hint (-5 points)")
                    print("  skip                - Skip this task (-10 points)")
                    print("  ref [command]       - Show command reference")
                    print("  status              - Show your progress")
                    print("  achievements        - Show unlocked achievements")
                    print("  stats               - Show detailed statistics")
                    print("  whatlearned         - Show what you've learned")
                    print("  quit/exit/q         - Exit the game")
                    input("\nPress Enter to continue...")
                    continue

                elif user_input.lower() == 'whatlearned':
                    self.show_what_learned()
                    continue

                elif user_input.lower().startswith('ref'):
                    parts = user_input.split()
                    if len(parts) > 1:
                        self.show_command_reference(parts[1])
                    else:
                        self.show_command_reference(None)
                    continue

                elif user_input.lower() == 'hint':
                    self.print_colored(f"\n💡 Hint: {level['hint']}", Colors.YELLOW, True)
                    self.hints_used += 1
                    level_hints += 1
                    self.score -= 5
                    self.save_game()
                    input("\nPress Enter to continue...")
                    continue

                elif user_input.lower() == 'skip':
                    print("\n⏭️ Skipping task... (-10 points)")
                    current_task['completed'] = True
                    self.score -= 10
                    self.streak = 0
                    self.save_game()
                    input("Press Enter to continue...")
                    continue

                elif user_input.lower() == 'status':
                    self.show_status()
                    continue

                elif user_input.lower() == 'achievements':
                    self.show_achievements()
                    continue

                elif user_input.lower() == 'stats':
                    self.show_stats()
                    continue

                self.total_attempts += 1

                if self.validate_command(user_input, current_task['check']):
                    self.correct_attempts += 1
                    self.streak += 1
                    if self.streak > self.max_streak:
                        self.max_streak = self.streak

                    self.print_colored("\n✅ Correct! Task completed!", Colors.GREEN, True)
                    self.simulate_command(user_input)
                    current_task['completed'] = True

                    streak_bonus = 0
                    if self.streak >= 5:
                        streak_bonus = self.streak * 2
                        self.print_colored(f"🔥 Streak bonus! +{streak_bonus} points", Colors.RED)

                    self.score += 20 + streak_bonus
                    self.xp += 10 + streak_bonus//2
                    self.command_history.append(user_input)
                    self.save_game()
                    self.check_achievements()
                else:
                    self.streak = 0
                    self.print_colored(f"\n❌ Wrong command!", Colors.RED, True)
                    self.print_colored(f"💡 Tip: Try using: {Colors.CYAN}{current_task['check']}{Colors.RESET}", Colors.YELLOW)
                    self.score -= 2

                input("\nPress Enter to continue...")

        return False

    def show_what_learned(self):
        self.clear_screen()
        self.print_header()
        self.print_colored("\n📖 WHAT YOU'VE LEARNED SO FAR", Colors.CYAN, True)
        print("-" * 85)
        for level_num in sorted(self.completed_levels):
            if level_num in LEVELS:
                level = LEVELS[level_num]
                print(f"✅ Level {level_num}: {level['name']}")
                print(f"   {Colors.DIM}→ {level['what_you_learn']}{Colors.RESET}")
        if not self.completed_levels:
            print("You haven't completed any levels yet!")
        input("\nPress Enter to continue...")

    def show_status(self):
        self.clear_screen()
        self.print_header()
        print(f"\n📊 {Colors.BOLD}Player Status{Colors.RESET}")
        print("-" * 50)
        print(f"👤 Name: {self.username}")
        print(f"🏆 Score: {Colors.YELLOW}{self.score}{Colors.RESET}")
        print(f"⭐ XP: {Colors.BLUE}{self.xp}{Colors.RESET}")
        print(f"📍 Level: {self.current_level}/50")
        print(f"🔥 Current Streak: {Colors.RED}{self.streak}{Colors.RESET}")
        print(f"🔥 Max Streak: {Colors.RED}{self.max_streak}{Colors.RESET}")
        print(f"💡 Hints Used: {self.hints_used}")
        print(f"✅ Completed Levels: {len(self.completed_levels)}/50")
        print(f"🏅 Achievements: {len(self.achievements)}/{len(ACHIEVEMENTS)}")
        print(f"📊 Accuracy: {self.get_accuracy()}%")
        print(f"⏱️  Total Play Time: {self.get_play_time()}")
        print(f"🎮 Mode: {self.game_mode}")

        beginner = sum(1 for l in self.completed_levels if LEVELS[l]['category'] == "Beginner")
        intermediate = sum(1 for l in self.completed_levels if LEVELS[l]['category'] == "Intermediate")
        advanced = sum(1 for l in self.completed_levels if LEVELS[l]['category'] == "Advanced")
        expert = sum(1 for l in self.completed_levels if LEVELS[l]['category'] == "Expert")
        master = sum(1 for l in self.completed_levels if LEVELS[l]['category'] == "Master")

        print(f"\n📈 {Colors.BOLD}Category Progress{Colors.RESET}")
        print(f"  Beginner:    {beginner}/10  {'█' * beginner}{'░' * (10 - beginner)}")
        print(f"  Intermediate: {intermediate}/10 {'█' * intermediate}{'░' * (10 - intermediate)}")
        print(f"  Advanced:    {advanced}/10   {'█' * advanced}{'░' * (10 - advanced)}")
        print(f"  Expert:      {expert}/10     {'█' * expert}{'░' * (10 - expert)}")
        print(f"  Master:      {master}/10     {'█' * master}{'░' * (10 - master)}")

        input("\nPress Enter to continue...")

    def show_achievements(self):
        self.clear_screen()
        self.print_header()
        self.print_colored("\n🏅 ACHIEVEMENTS", Colors.MAGENTA, True)
        print("-" * 50)
        for key, ach in ACHIEVEMENTS.items():
            status = "✅" if key in self.achievements else "🔒"
            print(f"  {status} {ach['icon']} {ach['name']} - {ach['desc']}")
        input("\nPress Enter to continue...")

    def show_stats(self):
        self.clear_screen()
        self.print_header()
        self.print_colored("\n📊 DETAILED STATISTICS", Colors.CYAN, True)
        print("-" * 50)
        print(f"Total Attempts: {self.total_attempts}")
        print(f"Correct Answers: {self.correct_attempts}")
        print(f"Accuracy: {self.get_accuracy()}%")
        print(f"Total XP: {self.xp}")
        print(f"Total Score: {self.score}")
        print(f"Max Streak: {self.max_streak}")
        print(f"Total Play Time: {self.get_play_time()}")

        print(f"\n📈 {Colors.BOLD}Level Performance{Colors.RESET}")
        for level_num in sorted(self.level_stats.keys())[-10:]:
            stats = self.level_stats[level_num]
            if stats.get('completed', False):
                time_str = f"{int(stats['time'])}s"
                hints = stats.get('hints_used', 0)
                score = stats.get('score', 0)
                mode = stats.get('mode', 'normal')
                print(f"  Level {level_num:2}: {time_str:5} | {hints} hints | {score:3} pts | {mode}")

        if self.command_history:
            print(f"\n📝 {Colors.BOLD}Command History (Last 10){Colors.RESET}")
            for i, cmd in enumerate(self.command_history[-10:], 1):
                print(f"  {i}. {cmd}")

        input("\nPress Enter to continue...")

    def about(self):
        self.clear_screen()
        self.print_header()
        print(f"\n🐧 {Colors.BOLD}LINUX CTF CHALLENGE - 50 Level Ultimate Edition{Colors.RESET}")
        print("=" * 60)
        print("Complete Linux learning journey from absolute beginner to expert!")
        print(f"\n📚 {Colors.BOLD}Features:{Colors.RESET}")
        print("  🎮 50 progressive levels")
        print("  📖 Each level has 'What You'll Learn'")
        print("  🏆 15+ achievements to unlock")
        print("  🔥 Streak system for bonus points")
        print("  ⚡ Time Attack mode")
        print("  📚 Built-in command reference")
        print("  💾 Auto-save progress")
        print("  📊 Detailed statistics")
        print(f"\n🎯 {Colors.BOLD}Learning Path:{Colors.RESET}")
        print("  Levels 1-10:  Beginner (Basic commands)")
        print("  Levels 11-20: Intermediate (System management)")
        print("  Levels 21-30: Advanced (Admin & networking)")
        print("  Levels 31-40: Expert (DevOps & cloud)")
        print("  Levels 41-50: Master (Everything combined)")
        print("=" * 60)
        input("\nPress Enter to continue...")

    def victory_screen(self):
        self.clear_screen()
        self.print_header()
        print("\n" + "🎉" * 40)
        self.print_colored("🏆 CONGRATULATIONS! YOU'VE COMPLETED ALL 50 LEVELS! 🏆", Colors.GREEN, True)
        print("🎉" * 40)
        self.print_colored(f"\n🐧 {Colors.BOLD}You are now a Linux Master!{Colors.RESET}")
        print(f"\n📊 {Colors.BOLD}Final Statistics:{Colors.RESET}")
        print(f"  👤 Player: {self.username}")
        print(f"  🏆 Final Score: {Colors.YELLOW}{self.score}{Colors.RESET}")
        print(f"  ⭐ Total XP: {Colors.BLUE}{self.xp}{Colors.RESET}")
        print(f"  📍 Levels Completed: 50/50")
        print(f"  💡 Hints Used: {self.hints_used}")
        print(f"  🔥 Max Streak: {Colors.RED}{self.max_streak}{Colors.RESET}")
        print(f"  📊 Accuracy: {self.get_accuracy()}%")
        print(f"  🏅 Achievements: {len(self.achievements)}/{len(ACHIEVEMENTS)}")
        print(f"  ⏱️  Total Play Time: {self.get_play_time()}")

        if self.achievements:
            print(f"\n{Colors.MAGENTA}🏅 Your Achievements:{Colors.RESET}")
            for ach in self.achievements:
                if ach in ACHIEVEMENTS:
                    a = ACHIEVEMENTS[ach]
                    print(f"  {a['icon']} {a['name']} - {a['desc']}")

        print("\n" + "=" * 85)
        self.print_colored("🎊 You are now officially a Linux Master! 🎊", Colors.CYAN, True)
        self.running = False
        sys.exit(0)

    def host_learning_portal(self):
        """Host the bundled LEARN WITH N4MR3S portal locally."""
        portal_dir = Path(__file__).resolve().parent / "portal"
        index_file = portal_dir / "index.html"

        if not index_file.exists():
            self.print_colored(
                "\n❌ Portal files were not found!",
                Colors.RED,
                True
            )
            print(f"Expected portal folder: {portal_dir}")
            print("Keep the 'portal' folder beside this Python file.")
            input("Press Enter to continue...")
            return

        class QuietHandler(SimpleHTTPRequestHandler):
            def log_message(self, format, *args):
                pass

        # Use a fixed local port so the browser keeps the same origin.
        # localStorage is origin-specific, and the port is part of the origin.
        # Using a random port (0) would create a new storage area on every run.
        server_port = 8000

        try:
            server = ThreadingHTTPServer(("127.0.0.1", server_port), QuietHandler)
        except OSError as e:
            self.print_colored(
                f"\n❌ Could not start the portal on port {server_port}.",
                Colors.RED,
                True
            )
            print("The fixed portal port may already be in use.")
            print(f"Try: lsof -i :{server_port}")
            print(f"Then stop the process if appropriate, and run the game again.")
            print(f"Error: {e}")
            input("Press Enter to continue...")
            return

        # SimpleHTTPRequestHandler serves from the process cwd by default.
        # Change only for the server thread, then restore it after shutdown.
        old_cwd = os.getcwd()
        os.chdir(str(portal_dir))

        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()

        url = f"http://127.0.0.1:{server_port}/"
        self.clear_screen()
        self.print_header()
        self.print_colored("\n🌐 LEARN WITH N4MR3S — LOCAL LEARNING PORTAL", Colors.CYAN, True)
        print("-" * 85)
        print("✅ Portal started successfully!")
        print(f"🌐 URL: {url}")
        print()
        print("The portal is running only on this computer.")
        print("Your browser stores portal progress locally.")
        print()
        print("Keep this game open while using the portal.")
        print("Press Ctrl+C in this terminal only when you want to stop the portal.")

        try:
            webbrowser.open(url)
            input("\nPress Enter to stop the portal and return to the game...")
        except KeyboardInterrupt:
            pass
        finally:
            server.shutdown()
            server.server_close()
            os.chdir(old_cwd)
            self.print_colored("\n🛑 Local portal stopped.", Colors.YELLOW, True)
            input("Press Enter to continue...")

    def main_menu(self):
        while self.running:
            self.clear_screen()
            self.print_header()

            if not self.username:
                print("\n📋 {Colors.BOLD}MAIN MENU{Colors.RESET}")
                print("-" * 50)
                print("1. 🆕 Start New Game")
                print("2. 💾 Load Saved Game")
                print("3. 📖 What You'll Learn")
                print("4. 🌐 Host LEARN WITH N4MR3S Portal Locally")
                print("5. ℹ️  About")
                print("6. 🚪 Exit")
                print("-" * 50)

                choice = input("Select option (1-6): ").strip()

                if choice == '1':
                    self.username = input("Enter your name: ").strip()
                    if not self.username:
                        self.username = "Player"
                    self.current_level = 1
                    self.score = 0
                    self.xp = 0
                    self.hints_used = 0
                    self.completed_levels = []
                    self.achievements = []
                    self.streak = 0
                    self.max_streak = 0
                    self.total_attempts = 0
                    self.correct_attempts = 0
                    self.level_stats = {}
                    self.command_history = []
                    self.total_play_time = 0
                    self.start_time = time.time()
                    self.save_game()
                    self.print_colored(f"\n✅ Welcome, {self.username}! Let's begin your 50-level journey!", Colors.GREEN, True)
                    print(f"📖 You'll learn everything from basic commands to advanced Linux administration!")
                    input("Press Enter to start...")

                    while self.running and self.current_level <= 50:
                        if self.current_level not in LEVELS:
                            self.current_level += 1
                            continue
                        if not self.play_level(self.current_level):
                            break

                    if self.current_level > 50:
                        self.victory_screen()

                elif choice == '2':
                    if self.load_game():
                        self.print_colored(f"\n✅ Welcome back, {self.username}!", Colors.GREEN, True)
                        print(f"📍 Level: {self.current_level}/50")
                        print(f"🏆 Score: {self.score}")
                        input("Press Enter to continue...")
                        while self.running and self.current_level <= 50:
                            if self.current_level not in LEVELS:
                                self.current_level += 1
                                continue
                            if not self.play_level(self.current_level):
                                break
                        if self.current_level > 50:
                            self.victory_screen()
                    else:
                        self.print_colored("\n❌ No saved game found!", Colors.RED, True)
                        input("Press Enter to continue...")

                elif choice == '3':
                    self.show_all_what_learned()

                elif choice == '4':
                    self.host_learning_portal()

                elif choice == '5':
                    self.about()

                elif choice == '6':
                    self.print_colored("\n👋 Goodbye!", Colors.CYAN, True)
                    self.running = False
                    sys.exit(0)

            else:
                print(f"\n👋 Welcome back, {self.username}!")
                print(f"📍 Level: {self.current_level}/50")
                print(f"🏆 Score: {self.score}")
                print(f"⭐ XP: {self.xp}")

                print("\n📋 {Colors.BOLD}GAME MENU{Colors.RESET}")
                print("-" * 50)
                print("1. 🎮 Continue Game")
                print("2. 📊 View Progress")
                print("3. 🏅 Achievements")
                print("4. 📈 Statistics")
                print("5. 📚 Command Reference")
                print("6. 📖 What You've Learned")
                print("7. ⚙️  Game Settings")
                print("8. 🔄 Reset Game")
                print("9. 🌐 Host LEARN WITH N4MR3S Portal Locally")
                print("10. ℹ️  About")
                print("11. 🚪 Exit")
                print("-" * 50)

                choice = input("Select option (1-11): ").strip()

                if choice == '1':
                    while self.running and self.current_level <= 50:
                        if self.current_level not in LEVELS:
                            self.current_level += 1
                            continue
                        if not self.play_level(self.current_level):
                            break
                    if self.current_level > 50:
                        self.victory_screen()

                elif choice == '2':
                    self.show_status()

                elif choice == '3':
                    self.show_achievements()

                elif choice == '4':
                    self.show_stats()

                elif choice == '5':
                    self.show_command_reference(None)

                elif choice == '6':
                    self.show_what_learned()

                elif choice == '7':
                    self.game_settings()

                elif choice == '8':
                    confirm = input("⚠️  Reset all progress? (yes/no): ")
                    if confirm.lower() == 'yes':
                        save_file = os.path.expanduser("~/.linux_ctf_50.json")
                        if os.path.exists(save_file):
                            os.remove(save_file)
                        self.username = ""
                        self.current_level = 1
                        self.score = 0
                        self.xp = 0
                        self.hints_used = 0
                        self.completed_levels = []
                        self.achievements = []
                        self.streak = 0
                        self.max_streak = 0
                        self.total_attempts = 0
                        self.correct_attempts = 0
                        self.level_stats = {}
                        self.command_history = []
                        self.total_play_time = 0
                        self.start_time = time.time()
                        self.print_colored("✅ Game reset successfully!", Colors.GREEN, True)
                        input("Press Enter to continue...")

                elif choice == '9':
                    self.host_learning_portal()

                elif choice == '10':
                    self.about()

                elif choice == '11':
                    self.print_colored("\n👋 Goodbye!", Colors.CYAN, True)
                    self.running = False
                    sys.exit(0)

    def show_all_what_learned(self):
        self.clear_screen()
        self.print_header()
        self.print_colored("\n📖 WHAT YOU'LL LEARN IN ALL 50 LEVELS", Colors.CYAN, True)
        print("-" * 85)
        for level_num in sorted(LEVELS.keys()):
            level = LEVELS[level_num]
            status = "⭐" if level_num in self.completed_levels else "  "
            print(f"{status} Level {level_num:2}: {level['name'][:25]:25} → {level['what_you_learn']}")
        input("\nPress Enter to continue...")

    def game_settings(self):
        while True:
            self.clear_screen()
            self.print_header()
            self.print_colored("\n⚙️  GAME SETTINGS", Colors.CYAN, True)
            print("-" * 50)
            print(f"1. 🎮 Game Mode: {self.game_mode}")
            print("2. 🔙 Back")
            print("-" * 50)

            choice = input("Select option (1-2): ").strip()

            if choice == '1':
                print("\nAvailable modes:")
                print("  normal    - Standard gameplay")
                print("  time_attack    - Time Attack mode (bonus for speed)")
                new_mode = input("Enter mode name: ").strip().lower()
                if new_mode in ['normal', 'time_attack']:
                    self.game_mode = new_mode
                    self.save_game()
                    self.print_colored(f"✅ Mode changed to: {self.game_mode}", Colors.GREEN, True)
                else:
                    self.print_colored("❌ Invalid mode", Colors.RED, True)
                input("Press Enter to continue...")
            elif choice == '2':
                break

# ============================================
# MAIN ENTRY POINT
# ============================================

def main():
    try:
        game = CTFGame()
        game.main_menu()
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for playing!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Please make sure Python 3 is installed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
