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
    SESSION = "BQCUT1iRXbmWOripY6RpR1UdZKy290BrxfElVW--fdYhOVUh9izHKH7ISJ3ZLKu35hZGu4cZSXvCOdGvpz2iMbZu9BEIB2LJmCeR34Wxgw_OTo8KBqITy5tNtbRYT1oS2iowf8kMA9Tt7iDiX0KZ8QRRYB8nj6ouvFe79eyG8Rz-NazBWFgpkECZ305yReefBwNRtaqdwMofLeIYJtfFRwnelkwXQIrgicn3MrWqS398gsBNy6fsLe5dhRT4Bfv_GEsCduvLjgwc0Uu3s_SLdIvHzs3GArYV87dSLy7ISmVZ-1tRheaLjkd-ExO8iS1hSc3rezQ00CKiDX54Qx5oZFPxJBocyAA"
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
