Django 연습 파일

# 설치 및 실행

```bash
# 폴더 만들고 들어가기
mkdir <folder name>
cd <folder name>
```

```python
# 가상환경 만들기
python -m venv venv
# -m : 모듈을 만들겠다
# venv : venv모듈을
# venv : venv 이름으로
```





## 실행_1

```python
# 가상환경 실행
source venv/Scripts/activate
# (venv)가 뜨면 성공
# 꺼지면 활성화를 다시 해야함
```



## 설치_1

```bash
pip install django
django-admin startproject <project name> .

# 장고야 나는 현재 폴더에다가 프로젝트를 시작할꺼야 파일명은 <project name> 
# . -> 현재 폴더 에다가
```



## 설치_2_django_shell

```bash
pip install django-extensions
# 이미 한번 해서 계속 안해도 된다
```









## 실행_2

```python
python manage.py runserver
# 로컬호스트로 만들어진 url => 127.0.0.1
```



## 실행 겸 설치(migration)

```python
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# 위의 클래스를 만들었다면
# 밑의 마이그래이션을 실행하여야 함
python manage.py makemigrations
python manage.py migrate
```







## admin 아이디 비밀번호 생성

```bash
$ python manage.py createsuperuser

Username (leave blank to use 'tmddu'): admin
	# 일반적으로 admin을 사용 (사용안해도 상관 없음)
Email address: 
	# 없어도 상관 없음
Password: 
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
	# 경고문구
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
(venv) 
```





