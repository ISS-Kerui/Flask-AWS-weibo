# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo
from application.models import User
from flask_login import current_user


class LoginForm(Form):
    """
    用户登录表单
    """
    email = StringField(validators=[DataRequired(message='Email cannot be empty'), Email(message='Incorrect email format'), Length(1, 64)])
    password = PasswordField(validators=[DataRequired(message='Email cannot be empty'), Length(1, 64)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegistrationForm(Form):
    """
    用户注册表单
    """
    email = StringField('', validators=[DataRequired(message='Email cannot be empty'), Email(message='Incorrect email format'), Length(1, 64, message='The email name is too long')])
    username = StringField(
        '',
        validators=[
            DataRequired(message='Username cannot be empty'), Length(1, 64, message='The name is too long'),
            Regexp(
                '^[A-Za-z][A-Za-z0-9]*$',
                0,
                'Username must be made up of letters and Numbers')
        ])
    password = PasswordField('', validators=[DataRequired(message='Password cannot be empty'), Length(1, 64, message='Password is too long')])
    submit = SubmitField('Sign Up')

    def validate_email(self, field):
        """
        :summary: 检测邮箱是否已经被注册
        :param field:
        :return:
        """
        user = User.query.filter_by(email=field.data).first()
        if user is not None:
            raise ValidationError('The email address has been used')

    def validate_username(self, field):
        """
        :summary: 检测用户名是否已经被使用
        :param field:
        :return:
        """
        user = User.query.filter_by(username=field.data).first()
        if user is not None:
            raise ValidationError('The username has been used')


class ChangePasswordForm(Form):
    """
    用户修改密码表单
    """
    current_password = PasswordField(validators=[DataRequired(message='Password cannot be empty'), Length(1, 64)])
    new_password = PasswordField(
        validators=[
            DataRequired(message='Password cannot be empty'), Length(1, 64, message='The password is too long'),
            EqualTo('confirm_new_password', message='Two passwords do not match')
        ])
    confirm_new_password = PasswordField(validators=[DataRequired(message='Password cannot be empty')])
    submit = SubmitField('Save the changes')

    def validate_current_password(self, field):
        if not current_user.verify_password(field.data):
            raise ValidationError('The current password is incorrect')


class ResetPasswordRequestForm(Form):
    """
    重设密码请求的表单
    """
    email = StringField(
        validators=[
            DataRequired(message='Email cannot be empty'),
            Email(message='Incorrect email format'),
            Length(1, 64, message='The email address is too long')
        ])
    submit = SubmitField('Reset email')

    def validate_email(self, field):
        """
        :summary: 检测邮箱是否已经被注册
        :param field:
        :return:
        """
        user = User.query.filter_by(email=field.data).first()
        if user is None:
            raise ValidationError('The account does not exist. Please check the email address you entered')


class ResetPasswordForm(Form):
    """
    重设密码表单
    """
    email = StringField(
        validators=[
            DataRequired(message='Email cannot be empty'),
            Email(message='Incorrect email format'),
            Length(1, 64, message='The email address is too long')
        ])
    new_password = PasswordField(
        validators=[
            DataRequired(message='Password cannot be empty'), Length(1, 64, message='The password is too long'),
            EqualTo('confirm_new_password', message='Two input password must be consistent')
        ])
    confirm_new_password = PasswordField(validators=[DataRequired(message='Password cannot be empty')])
    submit = SubmitField('Reset Password')

    def validate_email(self, field):
        """
        :summary: 检测邮箱是否已经被注册
        :param field:
        :return:
        """
        user = User.query.filter_by(email=field.data).first()
        if user is None:
            raise ValidationError('The account does not exist. Please check the email address you entered')


class EditProfileForm(Form):
    """
    用户级别的资料编辑器
    """
    username = StringField('Nick Name', validators=[DataRequired(message="Nickname cannot be empty"), Length(1, 64, message='The name is too long')])
    real_name = StringField('Real Name', validators=[Length(0, 64, message='The name is too long')])
    location = StringField('City', validators=[Length(0, 64, message='The city name is too long')])
    about_me = StringField('Self-introduction', validators=[Length(0, 512, message='The introduction is too long')])
    submit = SubmitField('Save changes')













