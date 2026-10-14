# BA Quest Optimizer

**BA Quest Optimizer** is a small automation tool for performing daily activities in **Blue Archive**.

The idea is simple: configure the activities you want to perform once in `config.yaml`, start the game, and leave it running for around 15 minutes. The script will perform the configured activities automatically while you can do something else.

> **⚠️ Work in Progress**
>
> This project is still under development. Many features are not implemented yet or have not been thoroughly tested. Some actions may be unreliable, and some activities may currently take longer to complete than doing them manually.
>
> The main goal of this project is **not speed**, but convenience — start the routine and let the script handle it while you do something else.

## ⚠️ Disclaimer

BA Quest Optimizer is an **unofficial third-party project** and is not affiliated with, endorsed by, or associated with the developers or publisher of Blue Archive.

Using automation software may potentially violate the game's Terms of Service. **Use this project at your own risk.** The author does not guarantee that using this software will not result in a ban or any other action being taken against your account.

The project is designed to automate simple interactions with the game's user interface and does not attempt to modify the game's files, memory, or internal data.

## 📦 Installation

> **⚠️ You should have Python installed on your system and added to PATH. Python 3.11 is recommended.**

### 1. Extract the archive

Extract the downloaded archive to a location of your choice.

### 2. Install the dependencies

Run `install.bat`

### 3. Configure the script

Open `config.yaml` in any text editor.

The configuration file allows you to enable or disable the activities you want the script to perform.

For example:
```yaml
game_process: bluearchive.exe
game_window_title: Blue Archive

cafe:
  invite_cafe_1: False
  invite_cafe_2: False
  characters_touch_cafe_1: False
  characters_touch_cafe_2: False
```

Set an option to `True` to enable it, or `False` to disable it.

Once configured, you do not need to change the configuration before every run.
All options are described below in **Configuration**.

### 4. Start the script

Run `start.bat`

The script will start performing the activities enabled in `config.yaml`.

---

## 🤖 Currently Automated Activities

- Login
- Cafe
- Club

---

## ⚙️ Configuration

All settings are stored in `config.yaml`.

The configuration will grow as more activities are added to the project.

### Game settings

```yaml
game_process: bluearchive.exe
game_window_title: Blue Archive
logs_level: DEBUG

start_game: False
prepare_game: False
```

* `game_process` — the name of the Blue Archive process.
* `game_window_title` — the title of the game window.
* `logs_level` — determines the level of logs, ensure that you set it to `DEBUG` when providing logs while creating an issue.  
Possible values: `DEBUG`, `INFO`, `WARNING`
* `start_game` — if enabled, the script will launch the game through Steam
* `prepare_game` — if enabled, you can start the script right after the game started; otherwise, the script must be run when the game is on the main screen.

### Cafe

```yaml
cafe:
  collect_earnings: True
  invite_cafe_1: False
  invite_cafe_2: False
  characters_touch_cafe_1: False
  characters_touch_cafe_2: False
```

* `collect_earnings` — collect the cafe earnings
* `invite_cafe_1` — invites the first student from the list in cafe 1
* `invite_cafe_2` — invites the second student from the list in cafe 2 (⚠️may invite not the second student)
* `characters_touch_cafe_1` — clicks all the characters in cafe 1 (⚠️may skip some students, don't use yellow floor)
* `characters_touch_cafe_2` — clicks all the characters in cafe 2 (⚠️may skip some students, don't use yellow floor)

### Social

```yaml
social:
  club_reward_claim: True
```

* `club_reward_claim` — claims the club participation reward

---

## 🚧 Project Status

The project is currently in an early stage of development.

### Roadmap

⚠️ - may be unstable

- [x] Proceed to menu
- Cafe
  - [x] Earnings
  - [x] Invites ⚠️
  - [x] Student affection interactions ⚠️
- [ ] Lesson
- Social
  - [x] Club participation
  - [ ] Assistant collect
- [ ] Crafting
- [ ] Shop
- [ ] Bounty
- [ ] Scrimmage
- [ ] Tactical Challenge
- [ ] Free Daily Package
- [ ] Tasks rewards

---

## 🐛 Known Limitations

The automation relies on recognizing elements of the game's user interface.

Because of this, its reliability may depend on:

* screen resolution;
* Windows display scaling;
* changes to the Blue Archive interface;
* computer performance.

Changes to the game's UI may cause previously working automation to stop working; I will try to keep the script up to date.

If you encounter a problem, please create an Issue and include as much information as possible:

* what went wrong;
* logs file app.log located at the script root folder;
* any relevant error messages.

---

## ❤️ Why?

Daily activities in Blue Archive are usually simple, but they still require regular attention.

BA Quest Optimizer is intended to handle this repetitive routine for you.

Configure it once, start the game and the script, and let it take care of the daily activities while you do something else.

If you want to thank me, just press the star button

*It's not necessarily faster than doing everything manually — you just don't have to sit there and do it yourself.*