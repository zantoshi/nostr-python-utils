from secp256k1 import PrivateKey, PublicKey
import time, json, hashlib
from websocket import create_connection

def create_keypair():
    privkey = PrivateKey()
    privkey_ser = privkey.serialize()

    pubkey = privkey.pubkey
    pub = pubkey.serialize(compressed=True).hex()[2:]

    keypair = {
                "private_key" : privkey, 
                "pub_key" : pub
               }
    return keypair

def create_timestamp():
    ts = int(time.time())
    return ts

def get_event_kind(type):
    if type == "short_note":
        kind = 1
    elif type == "long_form":
        kind = 30023
    
    return kind


def create_event_id(pub, ts, kind, tags, content):
    # creating event_id
    # serialize
    # convert to bytes
    # encode to utf-8
    # hash
    # finally, hex. that creates the event_id
    event_data = json.dumps([0, pub, ts, kind, tags, content], separators=(',', ':'))
    event_id = hashlib.sha256(event_data.encode('utf-8')).hexdigest()
    return event_id

# creating signature
def create_signature(event_id, private_key):
    id_bytes = (bytes(bytearray.fromhex(event_id)))
    sig = private_key.schnorr_sign(id_bytes, bip340tag='', raw=True)
    sig = sig.hex()
    return sig

def broadcast_event(event):
    ws = create_connection("wss://relay.snort.social")

    ws.send(
        json.dumps(
            [
                "EVENT", 
                event
            ]
        ).encode('utf-8')
    )

    result =  ws.recv()
    print("Received '%s'" % result)
    ws.close()

def publish_short_note(keypair, content, tags):
    ts = create_timestamp()
    kind = get_event_kind("short_note")
    event_id = create_event_id(keypair["pub_key"], ts, kind, tags, content)
    sig = create_signature(event_id, keypair["private_key"])
    event = {"id":event_id,"pubkey":keypair["pub_key"],"created_at":ts,"kind":kind,"tags": tags,"content":content,"sig":sig}
    broadcast_event(event)

def publish_longform_note(keypair, content, tags):
    ts = create_timestamp()
    kind = get_event_kind("long_form")
    event_id = create_event_id(keypair["pub_key"], ts, kind, tags, content)
    sig = create_signature(event_id, keypair["private_key"])
    event = {"id":event_id,"pubkey":keypair["pub_key"],"created_at":ts,"kind":kind,"tags": tags,"content":content,"sig":sig}
    broadcast_event(event)