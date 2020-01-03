"""
С помощью паттерна "Наблюдатель" реализуйте простую систему подписок и уведомлений видеохостинга MyTube.

Для реализации можно использовать следующие определения классов:

MyTubeChannel - канал, у которого есть владелец.
    Параметры:
        name: str - Название канала
        owner: MyTubeUser - Владелец канала
        playlists: Dict[str, List[str]] - Плейлисты на канале ({'Название плейлиста': ['видео 1', 'видео 2', 'видео 3']})

    Методы:
        __init__(channel_name: str, chanel_owner: MyTubeUser) - При создании канала указывается название канала и его владелец
        subscribe(user: MyTubeUser) - Подписка пользователя user на канал
        publish_video(video: str) - Публикация нового видео и рассылка новости о публикации всем подписчикам
        publish_playlist(name: str, playlist: List[str]) - Публикация нового плейлиста и рассылка новости о публикации всем подписчикам

MyTubeUser - Пользователь видеохостинга MyTube
    Параметры:
        _name: str - Имя пользователя MyTube
    Методы:
        __init__(user_name: str) - У нового пользователя есть имя
        update(message: str): - Метод для приёма уведомлений о публикации

Пример кода, который должен работать:

matt = MyTubeUser('Matt')
john = MyTubeUser('John')
erica = MyTubeUser('Erica')

dogs_life = YoutubeChannel('All about dogs', matt)
dogs_life.subscribe(john)
dogs_life.subscribe(erica)

dogs_nutrition_videos = ['What do dogs eat?', 'Which Pedigree pack to choose?']
dogs_nutrition_playlist = {'Dogs nutrition': dogs_nutrition_videos}

for video in dogs_nutrition_videos:
    dogs_life.publish_video(video)

dogs_life.publish_playlist(dogs_nutrition_playlist)

Output:
Dear John, there is new video on 'All about dogs' channel: 'What do dogs eat?'
Dear Erica, there is new video on 'All about dogs' channel: 'What do dogs eat?'
Dear John, there is new video on 'All about dogs' channel: 'Which Pedigree pack to choose?'
Dear Erica, there is new video on 'All about dogs' channel: 'Which Pedigree pack to choose?'
Dear John, there is new playlist on 'All about dogs' channel: 'Dogs nutrition'
Dear Erica, there is new playlist on 'All about dogs' channel: 'Dogs nutrition'

"""

from abc import ABC, abstractmethod


class Observerable(ABC):

    @abstractmethod
    def subscribe(self, user):
        pass


class Observer(ABC):

    @abstractmethod
    def update(self, message: str) -> None:
        pass


class MyTubeChannel(Observerable):

    def __init__(self, name, owner):
        """
        :param name: name of channel
        :param owner: channel owner
        :param playlists: channel playlists
        """
        self.channel_name = name
        self.channel_owner = owner
        self.playlists = {}
        self.observers = list()

    def subscribe(self, user) -> None:
        """Subscribing user user to the channel

        :param user: user is Observer
        """
        self.observers.append(user)

    def publish_video(self, video) -> None:
        """Publish a new video and send news about
        the publication to all subscribers

        :param video:
        """
        for observer in self.observers:
            message = f"there is new video on '{self.channel_name}' channel: {video}"
            observer.update(message)

    def publish_playlist(self, playlist) -> None:
        """Publication of a new playlist and distribution
        of news about publication to all subscribers

        :param name:
        :param playlist:
        """
        self.playlists[self.channel_name] = playlist
        for observer in self.observers:
            for name_playlist, v in playlist.items():
                message = f"there is new playlist on '{self.channel_name}' channel: '{name_playlist}'"
                observer.update(message)


class MyTubeUser(Observer):

    def __init__(self, name):
        self._name = name

    def update(self, message) -> None:
        """Receive publication notifications

        :param message: message from MyTubeChannel
        """
        print(f"Dear {self._name}, {message}")


if __name__ == "__main__":
    matt = MyTubeUser('Matt')
    john = MyTubeUser('John')
    erica = MyTubeUser('Erica')

    dogs_life = MyTubeChannel('All about dogs', matt)
    dogs_life.subscribe(john)
    dogs_life.subscribe(erica)

    dogs_nutrition_videos = ['What do dogs eat?', 'Which Pedigree pack to choose?']
    dogs_nutrition_playlist = {'Dogs nutrition': dogs_nutrition_videos}

    for video in dogs_nutrition_videos:
        dogs_life.publish_video(video)

    dogs_life.publish_playlist(dogs_nutrition_playlist)