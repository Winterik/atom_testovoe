class ColorSorting:

    @staticmethod
    def sequence_sorting(sequence: str, colors: str) -> str:

        if not isinstance(sequence, str):  # проверка правильно переданных типов данных
            raise ValueError(f'Ожидается строка для sequence, получено: {type(sequence)}')
        if not isinstance(colors, str):
            raise ValueError(f'Ожидается строка для colors, получено: {type(colors)}')
        if len(colors) != 3 or len(
                set(colors)) != 3:  # проверка что нам пришла строка из уникальных символов ожидаемого размера
            raise ValueError('colors ожидается из трех уникальных цветов')

        for color in colors:  # Проверка, что все символы colors допустимы
            if not color.isalpha() or color not in 'ЗСК':
                raise ValueError(f'Недопустимый цвет в colors: {color}')

        color_number = {color: i for i, color in enumerate(colors)}  # маркируем цвета по важности

        for color in sequence:  # проверка на валидность цветов
            if color not in color_number:
                raise ValueError(f'Неизвестный цвет: {color}')

        sequence = list(sequence)  # временно преобразовываем строку в список
        low, mid, high = 0, 0, len(
            sequence) - 1  # указатели для цветов: low - зеленый, mid - текущая позиция, high - красный

        while mid <= high:  # цикл работает пока не дойдет до конца последовательности
            current_color = sequence[mid]  # берем цвет и сравниваем приоритеты
            if color_number[current_color] == 0:  # для зеленой проследовательности
                sequence[low], sequence[mid] = sequence[mid], sequence[low]
                low += 1
                mid += 1
            elif color_number[current_color] == 1:  # для синей последовательности
                mid += 1
            else:  # для красной последовательности
                sequence[mid], sequence[high] = sequence[high], sequence[mid]
                high -= 1

        return ''.join(sequence)  # собираем ответ обратно в строку