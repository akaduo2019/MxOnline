# users/forms.py

from django import forms
from captcha.fields import CaptchaField
from django.core.validators import RegexValidator

from .models import UserProfile


class LoginForm(forms.Form):
    '''登录验证表单'''

    username = forms.CharField(required=True,
                               validators=[
                                   RegexValidator(r"^[A-Z][0-9]{8}$", "请正确输入您的学号，首位大写")
                               ],
                               error_messages={
                                   'required': '账号不能为空'
                               },
                               )
    password = forms.CharField(required=True,
                               min_length=5,
                               max_length=20,
                               error_messages={
                                   'required': '密码不能为空',
                                   'min_length': '密码不能少于5位',
                                   'max_length': '密码不能超过20位',
                               },
                               )


class RegisterForm(forms.Form):
    '''注册验证表单'''

    # email = forms.EmailField(required=True)
    email = forms.CharField(required=True,
                            validators=[
                                RegexValidator(r"^[A-Z][0-9]{8}$", "请正确输入您的学号，首位大写")
                            ],
                            error_messages={
                               'required': '账号不能为空'
                            },
                            )
    password = forms.CharField(required=True,
                               min_length=5,
                               max_length=20,
                               error_messages={
                                   'required': '密码不能为空',
                                   'min_length': '密码不能少于5位',
                                   'max_length': '密码不能超过20位',
                               },
                               )
    # 验证码
    captcha = CaptchaField(error_messages={'required': '验证码不能为空',
                                           'invalid': '验证码错误'})

class ForgetPwdForm(forms.Form):
    '''忘记密码'''
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class ModifyPwdForm(forms.Form):
    '''重置密码'''
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)


class UploadImageForm(forms.ModelForm):
    '''用户更改图像'''
    class Meta:
        model = UserProfile
        fields = ['image']

class UserInfoForm(forms.ModelForm):
    '''个人中心信息修改'''
    class Meta:
        model = UserProfile
        fields = ['nick_name','gender','birthday','adress','mobile']
