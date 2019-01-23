<h1 align="center">
  <br>
    <img src="https://rawgit.com/jgchk/six-mans/master/sixmans/resources/icon.svg" alt="Six Mans" width="200">
  <br>
    Six Mans
  <br>
</h1>

<h4 align="center">A Discord bot for Rocket League 6-Mans queues.</h4>
<br>


## Key Features

* Queue handling
* Vote for or auto-pick captains
* Pick or randomly assign teams

## Installation

1. Clone the repository (```git clone https://github.com/Goregius/luff-scrims-bot```)
2. Install requirements (```pip install -r requirements.txt```)
3. Copy config.ini.example to config.ini in sixmans/config/
4. Enter your bot's token in the config.ini (<a href="https://discordapp.com/developers/applications/me">Create bot here</a>), and the id and worksheet of your Google Sheet.
5. Add a file called "credentials.json" in the root directory and add your Google API credientials (Service account key with Drive access) in there.
5. Run sixmans/bot.py

## Usage

1. Add yourself to the queue with the ```queue``` command
2. Once at least 6 people are in the queue, use one of the following commands to start a game:
    * ```voting```: Vote for captains
    * ```captains```: Randomly choose captains
    * ```random```: Randomly assign teams

## Commands

The default command prefix is ">". This can be changed in the config.
```
QUEUING
    queue
        description: Add yourself to the queue
        aliases: q

    dequeue
        description: Remove yourself from the queue
        aliases: dq

    kick <player>
        description: Remove another player from the queue
        example: kick @jgchk

TEAMMAKING
    voting
        description: Start a game by voting for captains

    captains
        description: Start a game by randomly choosing captains

    random
        description: Start a game by randomly assigning teams
```

---