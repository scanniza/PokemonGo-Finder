import json
from slackclient import SlackClient
import datetime

wanted_pokemon = None
sc = None
sc_channel_name = None

# Initialize object
def init():
    global sc, wanted_pokemon
    # load pushbullet key
    with open('config.json') as data_file:
        data = json.load(data_file)
        # get list of pokemon to send notifications for
        wanted_pokemon = _str( data["notify"] ) . split(",")
        # transform to lowercase
        wanted_pokemon = [a.lower() for a in wanted_pokemon]
        # get token
        token = _str( data["slack"] )
        sc_channel_name = _str( data["slack_channel_name"] )
        sc = SlackClient(token)



# Safely parse incoming strings to unicode
def _str(s):
  return s.encode('utf-8').strip()

# Notify user for discovered Pokemon
def pokemon_found(pokemon):
    # get name
    pokename = _str( pokemon["name"] ).lower()
    poketime = datetime.datetime.fromtimestamp(int(pokemon["disappear_time"])).strftime('%H:%M')
    address = "http://maps.google.com/maps?z=12&t=m&q=loc:"+str(pokemon["lat"])+"+"+str(pokemon["lng"])
    # check array
    if not pokename in wanted_pokemon: return

    # notify
    print "[+] Notifier found pokemon:", pokename
    text = "*"+_str(pokemon["name"]) + "* found! Disappears at: " + poketime + "\n<"+address+"|GOOGLE MAPS> <https://img.pokemondb.net/sprites/black-white/anim/normal/"+pokename+".gif| :pokeball:>"
    sc.api_call(
        "chat.postMessage", channel=sc_channel_name, text=text,
        username='PokemonHunter3000', icon_emoji=':pokeball:',
        mrkdwn=True
    )



init()
