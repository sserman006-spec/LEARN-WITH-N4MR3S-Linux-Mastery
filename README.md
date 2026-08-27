# 🏴 LEARN WITH N4MR3S — Linux Mastery

> **Learn Linux. Master the Terminal. Level Up.**

**LEARN WITH N4MR3S — Linux Mastery** is a gamified, hands-on Linux learning program created for **beginners, freshers, and students starting their Linux and cybersecurity journey**.

The goal is simple:

> **Don't just memorize commands. Run them, observe them, understand them, and use them to solve problems.**

The project combines a **50-level terminal-based learning game** with a **serverless web portal** for flag submission and progress tracking.

---

# 🎯 What Is LEARN WITH N4MR3S?

Linux is much easier to learn when you actually use it.

This project turns Linux learning into a structured progression:

```text
📖 Learn the concept
        ↓
💻 Practice in another terminal
        ↓
🧪 Experiment with commands
        ↓
🎯 Complete the task
        ↓
🚩 Find the flag
        ↓
🌐 Open the portal
        ↓
📋 Submit the flag
        ↓
✅ Flag verified
        ↓
⭐ Earn XP + 🏆 Points
        ↓
🔓 Next level unlocked
```

The levels are completed **sequentially**. Learners start from Level 1 and unlock the next level by successfully completing the current challenge.

---

# ⚠️ IMPORTANT — LEARN BY DOING

The game is designed to be used alongside a real Linux terminal.

When a level introduces a command:

1. Keep the learning game running.
2. Open **another terminal window/tab**.
3. Try the command yourself.
4. Try its options, flags, or switches.
5. Observe the output.
6. Understand what changed.
7. Return to the game and complete the task.

For example:

```bash
pwd
ls
cd ..
pwd
```

Don't simply copy commands.

Ask yourself:

```text
What does this command do?
Why is it useful?
What do its options/flags change?
What does the output tell me?
```

This project is intended to build **practical Linux knowledge**, not command memorization.

---

# 🚩 HOW FLAGS WORK

Each level has a corresponding flag.

The flag is a **completion checkpoint** for the practical task.

### The correct workflow is:

```text
Complete the task
      ↓
Find the flag
      ↓
Copy the flag
      ↓
Open LEARN WITH N4MR3S Portal
      ↓
Paste the flag into "Submit Flag"
      ↓
Submit
      ↓
Level completed
      ↓
Next level unlocked
```

### ❗ Do NOT paste the flag into the game terminal.

The game terminal is where you **perform the Linux task**.

The **web portal is where you submit the flag**.

---

# 🌐 LEARN WITH N4MR3S PORTAL

The repository contains a browser-based learning portal.

The portal is used to:

- 📊 Track learning progress
- 📚 View levels
- 🔒 See locked levels
- ✅ See completed levels
- 🚩 Submit discovered flags
- ⭐ Track XP
- 🏆 Track points
- 🔥 Track streaks
- 📈 View accuracy
- 🏅 View achievements

The portal is **serverless** and does not require a database.

---

# 🚀 QUICK START

## Requirements

You need:

- Linux
- Python 3
- A modern web browser

Check Python:

```bash
python3 --version
```

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/sserman006-spec/LEARN-WITH-N4MR3S-Linux-Mastery.git
```

Enter the project:

```bash
cd LEARN-WITH-N4MR3S-Linux-Mastery
```

---

## 2️⃣ Start the Learning Game

Run:

```bash
python3 learn_with_n4mr3s.py
```

The terminal game will start.

Choose:

```text
🆕 Start New Game
```

Enter your name and begin from **Level 1**.

---

# 🎮 USING THE GAME

Every level contains learning information and a practical task.

A typical level includes:

```text
📚 Level
📖 What you're learning
🎯 Objective
💡 Hints
🔧 Command reference
📌 Practical task
🚩 Flag
```

Useful built-in commands include:

```text
help
hint
ref <tool>
status
quit
```

Use these resources before asking an external platform how a command works.

The purpose of the project is to make the game itself useful as a learning resource.

---

# 🌐 HOST THE PORTAL LOCALLY

The game includes an option to host the portal locally.

Start the game:

```bash
python3 learn_with_n4mr3s.py
```

From the main menu, choose:

```text
🌐 Host LEARN WITH N4MR3S Portal Locally
```

The game will start a local web server and provide a local address for the portal.

Open that address in your browser.

---

# 🚩 SUBMITTING A FLAG

After discovering a flag:

### Step 1 — Copy the flag

Example:

```text
CTF{example_flag}
```

### Step 2 — Open the portal

Use:

```text
🌐 Host LEARN WITH N4MR3S Portal Locally
```

from the game menu.

### Step 3 — Open your current level

Find the level you are currently solving.

### Step 4 — Submit the flag

Use the portal's:

```text
🚩 Submit Flag
```

field.

Paste the flag and click:

```text
SUBMIT
```

### Step 5 — Continue

If the flag is correct, the portal will mark the level as completed and unlock the next stage.

---

# 🌍 ONLINE PORTAL — GITHUB PAGES

The web portal is also published as a static GitHub Pages site.

**LEARN WITH N4MR3S Portal:**

https://sserman006-spec.github.io/LEARN-WITH-N4MR3S-Linux-Mastery/

The online portal is useful for viewing the learning interface and progress features.

For the complete local learning experience, run the Python game and use its local portal option.

---

# 💾 PROGRESS TRACKING

The portal does not use a remote database.

Progress is stored locally in the browser using:

```text
localStorage
```

Conceptually:

```text
Browser
   ↓
localStorage
   ↓
Your progress
```

This means each learner can maintain their own progress without creating an online account.

### Progress is local to:

- Your browser
- Your device
- Your browser's stored site data

Clearing the browser's site data can remove locally stored progress.

---

# 📤 EXPORT & IMPORT PROGRESS

Use:

```text
📤 Export Progress
```

to create a backup of your progress.

Use:

```text
📥 Import Progress
```

to restore a previously exported backup.

This is useful when changing computers or browsers.

---

# 📚 50-LEVEL LEARNING PATH

The 50 levels progress from Linux fundamentals to advanced administration, infrastructure, automation, and security concepts.

## 🐧 Linux Foundations

- Terminal basics
- Filesystem navigation
- Directory creation
- File creation
- Reading files
- Copying and moving files
- Removing files
- Wildcards and patterns
- `grep`
- `find`
- File permissions
- Links
- Pipes and redirection
- Text processing

## ⚙️ System Administration

- Process management
- System information
- Advanced processes
- Network configuration
- Firewall management
- systemd
- Package management

## 💾 Storage

- Disk management
- LVM
- RAID

## 📡 Networking & Services

- SSH
- Remote access
- Web servers
- Databases
- DNS
- DHCP
- NFS
- Samba

## 📜 Scripting & Automation

- Bash scripting
- Advanced shell scripting
- Automation
- Text processing

## 🐳 Containers & Orchestration

- Docker
- Advanced Docker
- Kubernetes
- Advanced Kubernetes

## ☁️ DevOps, Cloud & Infrastructure

- CI/CD
- Cloud CLI
- Infrastructure as Code
- Monitoring
- Alerting
- Logging
- ELK stack

## 🛡️ Advanced Linux & Security

- Security hardening
- Performance tuning
- Advanced networking
- Virtualization
- Automation
- High availability
- Final Linux mastery challenge

---

# 🏆 GAMIFICATION

The program turns learning into a progression system.

Learners can earn:

```text
⭐ XP
🏆 Points
🔥 Streaks
🏅 Achievements
📊 Accuracy
📈 Progress
🚩 Completed flags
```

The objective is not to rush through the levels.

The objective is to **understand the concepts and build practical skill**.

---

# 📁 PROJECT STRUCTURE

The repository is intentionally kept as a **single repository**.

```text
LEARN-WITH-N4MR3S-Linux-Mastery/
│
├── README.md
├── index.html
├── learn_with_n4mr3s.py
│
└── portal/
    ├── index.html
    ├── style.css
    ├── app.js
    └── challenges.js
```

### `learn_with_n4mr3s.py`

The main terminal-based Linux learning game.

### `index.html`

The GitHub Pages entry point that directs visitors to the portal.

### `portal/index.html`

The main learning portal page.

### `portal/style.css`

Portal styling and user interface design.

### `portal/app.js`

Portal functionality, progress handling, flag submission, and local storage.

### `portal/challenges.js`

Challenge and level information used by the portal.

---

# 🌐 GITHUB PAGES ARCHITECTURE

The public portal works through a simple static structure:

```text
GitHub Pages
     │
     ▼
index.html
     │
     ▼
portal/
     │
     ├── index.html
     ├── style.css
     ├── app.js
     └── challenges.js
```

No backend server is required for the public portal.

---

# 🧑‍🎓 WHO IS THIS FOR?

LEARN WITH N4MR3S is intended for:

- Linux beginners
- College students
- Freshers
- Cybersecurity beginners
- CTF beginners
- Students preparing for cybersecurity labs
- Students interested in system administration
- Anyone who wants practical Linux experience

---

# 🧠 LEARNING PHILOSOPHY

The project follows:

> **Understand → Experiment → Practice → Solve → Discover → Progress**

When you learn a command, don't stop at its syntax.

Understand:

```text
What does it do?
Why is it useful?
What are its options?
What are its flags?
What happens when the input changes?
What does the output mean?
```

The second terminal is an important part of the learning process.

**Experiment. Break things safely. Observe. Learn.**

---

# ⚠️ SAFETY NOTICE

Some advanced Linux commands can modify:

- Files
- Filesystems
- Disks
- Network configuration
- Firewall rules
- Services
- System configuration

Do not blindly execute potentially destructive commands on an important personal system.

For advanced topics, use a:

```text
Virtual Machine
```

or another dedicated lab environment whenever possible.

Always understand commands before using elevated privileges such as `sudo`.

---

# 🤝 CONTRIBUTING

Suggestions, improvements, educational content, and bug reports are welcome.

You can contribute by:

- Reporting bugs
- Improving explanations
- Improving challenge instructions
- Adding beginner-friendly examples
- Suggesting missing Linux topics
- Improving the portal
- Submitting pull requests

---

# 🛣️ FUTURE LEARNING PATH

The Linux program can serve as the foundation for broader cybersecurity learning.

Possible future domains include:

```text
🌐 Web Exploitation
🔐 Cryptography
🔎 Digital Forensics
🖼️ Steganography
🌍 OSINT
🔬 Reverse Engineering
💥 Pwn / Binary Exploitation
🐧 Linux
🪟 Windows
🏢 Active Directory
📡 Networking
📦 Malware Analysis
🧠 Mobile Security
☁️ Cloud Security
🔑 Authentication & JWT
🗄️ Database Security
📱 Android
🍎 iOS
⛓️ Blockchain / Web3
🤖 AI Security
🔗 Hardware / IoT
🧩 Miscellaneous
🏆 Mixed CTF Challenges
```

These are potential extensions to the learning ecosystem; the current repository is focused on the **Linux Mastery** track.

---

# 🏴 LEARN WITH N4MR3S

## **Learn Linux. Master the Terminal. Level Up.**

Built to help beginners move from:

```text
"I don't know Linux"
```

to:

```text
"I understand what I'm doing in the terminal."
```

**Learn. Experiment. Solve. Discover. Progress.**
