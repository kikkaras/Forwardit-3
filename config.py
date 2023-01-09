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
    SESSION = "BQBdZXe3cHwcmzcMlcBUNJoHYHWQ-njATonkeN2CgKw6E2Kq5v4qlFwRAf1c5G6lEfoAivr_OoIxDOevtwlpAvxZQkq0ZPu4eoY6Aj70n9HURfA-Nd-c8T-F7v9Kx6K5KBX0jopZSHs63TmZqGwplWGgvgaLgnuduTunmHFeOpb0LPwnyTX_u66jaFXHKL8lzOXwsna20XQT_9Er67vzsscSLzhGBKlns513q_WNGhHOjiwktYGFDpbajCBUN5XIyeOd__MHDGkg-qhT44pDONW9DVpcLOVQhzjYSUGHBrYP-hk_LXgrhiWBylfBnWNhFINVjocgVV1ORp2_SXOcLwXxVm9SgwA"
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
