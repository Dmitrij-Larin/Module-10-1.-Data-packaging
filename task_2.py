import pickle


class MusicAlbums(object):

    def __init__(self, iterable=(), **kwargs):
        self.__dict__.update(iterable, **kwargs)

    def add_data(self, music_group, album):
        self.__dict__[music_group] = album
        return f"{self.__dict__}\nДобавлена группа {music_group} с альбомом \"{album}\"."

    def remove_data(self, music_group):
        if music_group in self.__dict__:
            del self.__dict__[music_group]
            return f"{self.__dict__}\nГруппа {music_group} удалена."
        else:
            return "Данной группы нет в словаре."

    def search_data(self, music_group):
        if music_group in self.__dict__:
            return f"Группа {music_group} и его альбом \"{self.__dict__[music_group]}\"."
        else:
            return "Данной группы нет в словаре."

    def change_data(self, music_group, new_album):
        if music_group in self.__dict__:
            self.__dict__[music_group] = new_album
            return f"{self.__dict__}\nТеперь здесь будет альбом \"{new_album}\" группы {music_group}."
        else:
            return "Данной группы нет в словаре."


class MyPickler:

    def __init__(self, protocol=pickle.DEFAULT_PROTOCOL):

        if protocol < 0 or protocol > 5:
            self.protocol = pickle.DEFAULT_PROTOCOL
        elif protocol == 0:
            self.protocol = pickle.HIGHEST_PROTOCOL
        else:
            self.protocol = protocol

    def pickle_data(self, data: object):
        pickled_data = pickle.dumps(data, self.protocol)
        return pickled_data

    def pickle_file(self, filename, data: object):
        with open(filename, 'wb') as fp:
            pickle.dump(data, fp, self.protocol)
        return f'Произведён пиклинг в файле {filename}'


class MyUnpickler:

    @classmethod
    def unpickle_data(cls, pickled_data):
        unpickle_data = pickle.loads(pickled_data)
        return unpickle_data

    @classmethod
    def unpickle_file(cls, pickled_filename):
        try:
            with open(pickled_filename, 'rb') as fp:
                unpickle_data = pickle.load(fp)
        except FileNotFoundError:
            return 'Файл не найден'
        return unpickle_data


if __name__ == '__main__':
    my_pickler_5 = MyPickler(protocol=5)
    my_pickler_default = MyPickler()

    music_albums = MusicAlbums({
        'Metallica': 'Master Of Puppets',
        'Megadeth': 'Rust And Peace',
        'Slayer': 'Reign In Blood',
        'Anthrax': 'Among The Living'
    })

    music_albums = my_pickler_5.pickle_data(music_albums)
    print()
    music_albums = MyUnpickler.unpickle_data(music_albums)
    print(music_albums.add_data('Pantera', 'Vulgar Display Of Power'))
    print()
    print(music_albums.remove_data('Anthrax'))
    print()
    print(music_albums.search_data('Megadeth'))
    print()
    print(music_albums.change_data('Slayer', 'Seasons Of Abyss'))

    my_pickler_default.pickle_file('info_music_album', music_albums)
    music_albums = MyUnpickler.unpickle_file('info_music_album.pkl')
