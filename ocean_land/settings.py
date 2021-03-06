"""
Django settings for ocean_land project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import datetime
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-aekl_c+8jk9_v6j_3gg$8a1hl569pn0v0ny6woe+7&rv=kw7@)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    # 开启跨域,顺序一般写在django自带app的下面，不能写在自己定义的子应用下面，不然会报错
    'corsheaders',
    # 自定义子应用
    'user',
    'interfaces',
    'projects',
    'envs',
    'configures',
    'debugtalk',
    'testcases',
    'testsuites',
    'reports',
    'summary',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# 跨域配置
# 允许前端使用所有的域名/IP访问后段接口
# CORS_ORIGIN_ALLOW_ALL=True
# #限制部分域名/ip才可以访问后端接口,这里要指定前后台的域名或者host+端口,只制定前端的域名不指定后段的域名也会报错
CORS_ORIGIN_WHITELIST = [
    # 前端访问host+端口
    'http://localhost:8080',
    'http://192.168.1.12:8080',
    # 后端访问host+端口
    'http://127.0.0.1:8000',
    'http://localhost:8000',

]

CORS_ALLOW_CREDENTIALS = True
ROOT_URLCONF = 'ocean_land.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ocean_land.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ocean_land1',
        'USER': 'root',
        'PASSWORD': 'li123456',
        'HOST': '106.14.220.57',
        'PORT': '3307'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    # 指定用于支持coreapi的schema
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    # 覆盖drf默认的认证。认证也可以在类视图中指定，但是认证一般都是全局指定
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # jwt token认证，顺序是先jwttoken-然后session，然后Basic
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # 支持账号密码进行认证
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    ],
    # 覆盖drf默认的授权，一般授权不需要全局指定，都是在类视图中指定
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    # 分页引擎
    # 'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_PAGINATION_CLASS': 'utils.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,

    # 当前搜索&&排序引擎配置全局生效
    'DEFAULT_FILTER_BACKENDS': ['rest_framework.filters.SearchFilter', 'rest_framework.filters.OrderingFilter'],
    # Filtering，修改查询字符串参数的key，默认key是search
    'SEARCH_PARAM': 'search1',
    'ORDERING_PARAM': 'ordering1',
}

# 添加日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s] %(message)s'}
    },
    'filters': {
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "logs/service.log"),  # 日志输出文件
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份份数
            'formatter': 'standard',  # 使用哪种formatters日志格式
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'mytest': {  # mytest，打印所有信息到名称为console的handler。
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}

# jwt认证相关配置
JWT_AUTH = {
    # 修改jwt的token中前缀
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    # 设置token的失效时间
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=3),
    #修改JWT认证之后接口返回
    'JWT_RESPONSE_PAYLOAD_HANDLER':'utils.jwt_payload_handler.jwt_response_payload_handler',
}

REPORT_DIR=os.path.join(BASE_DIR,'report')
SUITES_DIR=os.path.join(BASE_DIR,'suites')

