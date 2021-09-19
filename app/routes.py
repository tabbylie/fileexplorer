from app import app
from flask import render_template, request, redirect, make_response
import os
from os import path
import json
from os.path import join, dirname, realpath


def getfiles(directory, dirpath):
    folders = []
    files = []
    for filefolder in directory:
        filefoldertemp = path.join(dirpath, filefolder.strip())
        if path.isdir(filefoldertemp):
            folders.append(filefolder)
            continue
        files.append(filefolder)
    return (folders, files)


@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    # dirpath = path.join(os.environ['USERPROFILE'], 'Downloads') # testing!
    dirpath = '/root/ftpfolder'
    directory = request.cookies.get('currentFolder')
    lastFolder = request.cookies.get('prevFolder')
    if lastFolder == None:
        lastFolder = dirpath
    if directory == None:
        directory = dirpath
    directory = directory.replace('\\', '\\\\')
    dirpath = dirpath.replace('\\', '\\\\')
    if not directory.startswith(dirpath):
        directory = dirpath
    direct = os.listdir(directory)
    folders, files = getfiles(direct, directory)

    return render_template('index.html', folders=folders, files=files, lastfolder=lastFolder, currentFolder=directory)


@app.route('/set_cookie', methods=["GET", "POST"])
def set_cookie():
    if request.method == "POST":
        dic = request.get_json()
        direct = dic['filepath']
        resp = make_response(render_template('index.html'))
        resp.set_cookie('prevFolder', dic['currentFolder'])
        resp.set_cookie('currentFolder', direct)
        return resp
    return redirect('/')
