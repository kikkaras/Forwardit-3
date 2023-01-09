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
    SESSION = "BQBkNy9zPgNhrATo4ziQaXeWYC9EtIen7h_jgsXryKcLknkPZCX12moBpj0QNuAg_W-wvwVzAPKwlTpHJIRki9f_TVQ44HHzBW9GN3aQSjEHO5niJ455ZDwkxEBjImwGXVjx7CcirCEXWnfT269sgC5HBjDzGYZgkXMoWz1IWshbiRl-XNKzUtuIiNgJhKnNWagc0CsVtenXEBQWlFrJi4w7DtrSKO7Y830L1ZR8JKc7IQeCSiegquaF1PEhyb8JGoTirrg0fAi05tps3OkLMT5O_dVO_Bnjk3Y6TRGKxu8l8f-NFJ9jQO5u2Bt6zdkQRSiO9BnzvaJLQczWpjj6Y_ZuVm9SgwA"
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
