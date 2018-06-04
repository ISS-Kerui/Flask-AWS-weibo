# -*- coding: utf-8 -*-
from application import create_app, db
import os
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from application.models import User, Role, Permission, Post
from flask_uploads import UploadSet, configure_uploads, IMAGES

application = create_app(os.environ.get('CONFIG') or 'default')
manager = Manager(application)
migrate = Migrate(application, db=db)
application.config['UPLOADED_PHOTOS_DEST'] = './application/static/photos'
application.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
photos = UploadSet('photos',IMAGES)
configure_uploads(application, photos)

def make_shell_context():
    return dict(
        app=app,
        db=db, User=User, Role=Role, Permission=Permission,
        Post=Post
    )


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """
    :summary: 运行测试用例命令
    :return:
    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
