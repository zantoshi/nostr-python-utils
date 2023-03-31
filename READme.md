nostr-python-util
========

A set of useful things for [Nostr Protocol](https://github.com/nostr-protocol/nostr) implementations. The goal of this library is to keep this code relatively simple and based on a functional style of programming. This will be used for teaching and instruction purposes.

Create a virtual env by running.
`python3 -m venv env`
Then activate the virtual env. 
`source env/bin/activate`
Once you have activated the virtual environment, run the following installs.
```
pip3 install -U pip
pip3 install -U setuptools
pip3 install -r requirements.txt
```
Now you are all set to use the python util library.

Check out the nip-01 and nip-23 for example usage. Happy hacking! 

I plan to add to this library over-time as it is very basic for now.

An example of using this library to implement NIP-01 (short text notes):
```
from util import * 
keypair = create_keypair()

publish_short_note(keypair, "wss://relay.snort.social", "zbd rules", [["p", "4d992bd1e12f77866334ce3fdfe20203799bfefb84b7ed5cd111290345157b5a"]])
```

An example of using this implement NIP-23:
```
from util import * 
keypair = create_keypair()

publish_longform_note(keypair, "wss://relay.snort.social",
    '''
    ### ZBD Rules

    This is a test of the markdown functionality.
    ''', 
[
["p", "4d992bd1e12f77866334ce3fdfe20203799bfefb84b7ed5cd111290345157b5a"],
["title", "santos test"],
["published_at", str(create_timestamp())],
["t", "zbd"],
]
)
```