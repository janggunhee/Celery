import os
from celery import Celery

# 'Celery'프로그램의 기본 Django 설정 모듈을 설정합니다.
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'config.settings'
)

app = Celery('config')

# 여기서 문자열을 사용하는 것은 작업자가 직렬화 할 필요가 없음을 의미합니다.
#  자식 프로세스에 대한 설정 객체.
#  - namespace = 'CELERY'는 모든 샐러리 관련 구성 키를 의미합니다.
#  접두사는 'CELERY_'이어야합니다.
app.config_from_object(
    'django.conf:settings',
    namespace='CELERY'
)

# 등록 된 모든 Django app 설정에서 태스크 모듈을로드하십시오.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    # String format[r]: repr()
    print('Request: {0!r}'.format(self.request))
