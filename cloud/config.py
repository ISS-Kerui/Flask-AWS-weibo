# -*- coding: utf-8 -*-
import os
# 获取当前绝对路径
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    配置基类，包括所有环境都需要用到的配置。
    """
    # SECRET_KEY，Flask要求的配置键
    SECRET_KEY = 'KERUI' or os.environ.get('SECRET_KEY')
    # SQLALCHEMY_COMMIT_ON_TEARDOWN设置为True后每次请求结束都会自动提交数据库中的变动
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # SQLALCHEMY默认要求的配置，不然会有warning
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
    # 邮件相关配置，使用新浪邮箱
    MAIL_SERVER = 'imap.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'zhangkeruinuske@gmail.com'
    MAIL_PASSWORD = 'iv2105762'
    MAIL_DEFAULT_SENDER = 'zhangkeruinuske@gmail.com'
    EMAIL_PREFIX = '[Imitation-weibo]'
    POSTS_PER_PAGE = 15
    FOLLOWERS_PER_PAGE = 15

    @staticmethod
    def init_app(app):
        """
        :summary: 可以执行对当前环境的配置初始化。
        :param app: 程序实例
        :return:
        """
        pass


class DevelopmentConfig(Config):
    """
    开发环境配置类，继承了基类
    """
    DEBUG = True
    # Mysql数据库路径
    SQLALCHEMY_DATABASE_URI = 'username:password@localhost'


class TestingConfig(Config):
    """
    测试环境配置类，继承了基类
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost'


class ProductionConfig(Config):
    """
    生产环境配置类，继承了基类
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost'


config = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
