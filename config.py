#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @DarkzzAngel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "document")
    OWNER_ID = os.environ.get("OWNER_ID", 12345)
    SESSION = "BQChVlpK-cGUa9KI3bFo05zsf007VY4vzk154GVAmcyO9_NIw6b-Z5KqYx6ceY3J-z_ND_vNS_3TmGkPmmD2_E76Px3f1GdXQThi-kZ0IKs6Mf54RB5OGpsEpeajDZH3HmbVOYJqfg46a7uRR5SZY7hG4T6xqR7l7rERNTLz1pKVXBekIEh_gjaC9thMg6Lf4TwPCp5y7A357DtApZGeqTSJnmYWDHD6DfTAwp4bBEuMolmXDODFdKgKmLadojY59BYMth4CMjZQeiKA0Q0KcdyhdKf9SFeZsiE3UflLzptueA8oL_n-MvWa9fzkMCS8qBsXjwXvR80E60EwMKle4ZHEVm9SgwA"
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
