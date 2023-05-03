from user.models import User


def gen_master(apps, schema_editor):
    """
    유저 더미데이터
    """

    User.objects.create_superuser(
        username='admin',
        password='admin',
        name='관리자',
        email='',
    )

    for i in range(2, 4):
        username = f'user{i}'
        password = f'user{i}'
        name = f'이름{i}'
        email = ''

        User.objects.create_user(
            username=username,
            password=password,
            name=name,
            email=email,
        )