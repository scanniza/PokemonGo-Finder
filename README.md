# Pokemon Go Notification System

This is a fork of [the popular PokemonGo-Finder repository](https://github.com/jxmorris12/PokemonGo-Finder) with the purpose of allowing users to search for specific Pokemon without having to constantly monitor the map of nearby Pokemon. This allows users to set a list of sought-after Pokemon and receive notifications through [Slack](https://www.slack.com/). All API and map functionality was left untouched.

## Configure Slack
To generate a token for sending yourself notifications using the Slack API, go [here] (https://api.slack.com/web#authentication)

## Config File
Instead of from the command-line, all arguments are read from a `config.json` file. In addition to all of the options laid out [here](https://github.com/AHAAAAAAA/PokemonGo-Map/wiki/Usage), I've introduced three required fields: `slack`, your Pushbullet API key, `slack_channel_name`, which feels self-explanatory and `notify`, a comma-separated list of the Pokemon that you'd like to receive Slack notifications for.

Here's a sample `config.json`:

```
{
  "auth_service": "google",
  "username": "myemailuser",
  "password": "pikachu123",
  "step_limit": 5,
  "location": "742 Evergreen Terrace, Arlington, VA",
  "notify": "dratini,magnemite,electabuzz,hitmonchan,hitmonlee,chansey,lapras,snorlax,porygon,mew,mewtwo,moltres,zapdos,articuno,ditto,seel,gyarados,cubone",
  "slack": "xoxp-2621592322-32256533362-61445255476-ef0b6786ee",
  "slack_channel_name": "general"
  "timezone": "Europe/Stockholm"
}
```

## Install

Install the necessary dependencies (including the slack client) by running `pip install --upgrade -r requirements.txt`. Create a config file and then run the main script using `python main.py`.

*Using this software is against the ToS and can get you banned. Use at your own risk.*
