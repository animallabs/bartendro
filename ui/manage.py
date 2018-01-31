#!/usr/bin/env python
from werkzeug import script
import os

def make_app():
    from bartendro.application import BartendroUIServer
    print "is file0000-------------->", os.path.isfile('bartendro.db')
    return BartendroUIServer('sqlite:///bartendro.db')

def make_shell():
    from bartendro import models, utils
    application = make_app()
    return locals()

action_runserver = script.make_runserver(make_app, use_reloader=True)
action_shell = script.make_shell(make_shell)
action_initdb = lambda: make_app().init_database()

script.run()
