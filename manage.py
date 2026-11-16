#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# manage.py의 주요 역할
# 명령어	|	역할
# runserver	| 개발 서버 실행
# startapp	| 새로운 App 생성
# makemigrations	|	Model 변경사항을 마이그레이션 파일로 생성
# migrate	|	마이그레이션을 DB에 적용
# createsuperuser	|	관리자 계정 생성
# shell	|	Django 환경에서 Python 코드 실행
# test	|	테스트 실행
# check	| 	프로젝트 설정 및 구성 검사