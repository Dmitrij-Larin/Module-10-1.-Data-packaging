import pickle


class CountriesAndCapitals(object):

    def __init__(self, iterable=(), **kwargs):
        self.__dict__.update(iterable, **kwargs)

    def add_data(self, country, capital):
        self.__dict__[country] = capital
        return f"{self.__dict__}\nДобавлена страна {country} со столицей {capital}."

    def remove_data(self, country):
        if country in self.__dict__:
            del self.__dict__[country]
            return f"{self.__dict__}\nСтрана {country} удалена."
        else:
            return "Данной страны нет в словаре."

    def search_data(self, country):
        if country in self.__dict__:
            return f"Страна {country} и его столица {self.__dict__[country]}."
        else:
            return "Данной страны нет в словаре."

    def change_data(self, country, new_capital):
        if country in self.__dict__:
            self.__dict__[country] = new_capital
            return f"{self.__dict__}\nТеперь {new_capital} является столицей в {country}."
        else:
            return "Данной страны нет в словаре."


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

    countries_and_capitals = CountriesAndCapitals(
        {'Россия': 'Москва', 'Китай': 'Пекин', 'Германия': 'Берлин', 'Франция': 'Париж'})

    countries_and_capitals = my_pickler_5.pickle_data(countries_and_capitals)
    print()
    countries_and_capitals = MyUnpickler.unpickle_data(countries_and_capitals)
    print(countries_and_capitals.add_data('Великобритания', 'Лондон'))
    print()
    print(countries_and_capitals.remove_data('Германия'))
    print()
    print(countries_and_capitals.search_data('Китай'))
    print()
    print(countries_and_capitals.change_data('Россия', 'Санкт-Петербург'))

    my_pickler_default.pickle_file('info_countries_and_capitals', countries_and_capitals)
    countries_and_capitals = MyUnpickler.unpickle_file('info_countries_and_capitals.pkl')
