from util import * 
keypair = create_keypair()

publish_longform_note(keypair, 
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