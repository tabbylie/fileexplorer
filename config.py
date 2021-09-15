import os
from os.path import join, dirname, realpath

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "oO0x6^1aC3%1"
    ADMINS = ["abbylie121@gmail.com"]

    UPLOAD_FOLDER = os.path.join(basedir, "app/static/profile_imgs/")
