class User:
    def __init__(self, name, password, age):
        self.name = name
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.name


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.name = title
        self.duration = int(duration)
        self.time_now = int(time_now)
        self.adult_mode = adult_mode


class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.name:
                if user.password == hash(password):
                    self.current_user = user
                    break
                else:
                    print("Пароль неверный!\n")

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        flag = False
        for user in self.users:
            if user.name == nickname:
                flag = True
        if not flag:
            registering_user = User(nickname, password, age)
            self.users.append(registering_user)
            self.current_user = registering_user
        else:
            print(f"Пользователь {nickname} уже существует\n")

    def add(self, *args):
        for video in args:
            self.videos.append(video)

    def get_videos(self, key_word):
        searched_videos = []
        for video in self.videos:
            if str(key_word).lower() in str(video.name).lower():
                searched_videos.append(video.name)
        return searched_videos

    def watch_video(self, name):
        import time
        if self.current_user != None:
            for video in self.videos:
                if not video.adult_mode or (video.adult_mode and self.current_user.age >= 18):
                    if video.name == name:
                        while video.time_now <= video.duration:
                            print(video.time_now)
                            video.time_now += 1
                            time.sleep(1)
                        print("Конец видео")
                        video.time_now = 0
                else:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            print("Войдите в аккаунт, чтоб смотреть видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
