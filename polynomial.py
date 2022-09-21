class Polinomial:

    # создание экземпляра класса при различных входных данных (число, список, кортеж, экземпляр класса)
    def __init__(self, inp):
        if isinstance(inp, int) or isinstance(inp, float):
            self.coeffs = [inp]
            self.degr = 0
        elif isinstance(inp, Polinomial):
            self.coeffs = inp.coeffs
            self.degr = inp.degr
        elif isinstance(inp, tuple):
            self.coeffs = list(inp)
            self.degr = len(inp) - 1
        elif isinstance(inp, list):
            self.coeffs = inp
            self.degr = len(inp) - 1
        else:
            raise ValueError

    # преобразование к строке str(p) в стиле "x^2 + 2x - 4" (с пробелами или без),
    def __str__(self):
        res = ''
        if self.degr == 0:
            res = str(self.coeffs[0])
        else:
            for i in range(self.degr + 1):
                if i == self.degr:
                    res = res + \
                          ('' if (self.coeffs[i] == 0) else (
                                  (' + ' if (self.coeffs[i] >= 0) else ' - ') + str(abs(self.coeffs[i]))))
                elif i == self.degr - 1:
                    res = res + \
                          ('' if (self.coeffs[i] == 0) else ((' + ' if (self.coeffs[i] >= 0) else ' - ') + (
                              '' if (abs(self.coeffs[i]) == 1) else str(abs(self.coeffs[i]))) + 'x'))
                elif i == 0:
                    res = res + \
                          ('' if (self.coeffs[i] == 0) else (
                                  (('' if self.coeffs[i]>0 else '-') if (abs(self.coeffs[i]) == 1) else str(self.coeffs[i])) + 'x^' + str(
                              self.degr - i)))
                else:
                    res = res + \
                          ('' if (self.coeffs[i] == 0) else ((' + ' if (self.coeffs[i] >= 0) else ' - ') + (
                              '' if (abs(self.coeffs[i]) == 1) else str(abs(self.coeffs[i]))) + 'x^' + str(
                              self.degr - i)))
        return res

    # сложение, сложение с константой (с обеих сторон)
    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_self = self.coeffs.copy()
            new_self[self.degr] += other
            return Polinomial(new_self)
        elif isinstance(other, Polinomial):
            max_deg = max(self.degr + 1, other.degr + 1)
            new_self = ([0] * (max_deg - self.degr - 1))
            new_self.extend(self.coeffs)
            new_other = ([0] * (max_deg - other.degr - 1))
            new_other.extend(other.coeffs)
            for i in range(max_deg):
                new_self[i] += new_other[i]
            return Polinomial(new_self)
        else:
            raise ValueError

    def __radd__(self, other):
        return self + other

    # вычитание, вычитание с константой (с обеих сторон),
    def __sub__(self, other):
        return self + other * (-1)

    def __rsub__(self, other):
        return (self - other) * (-1)

    # умножение, умножение на константу (с обеих сторон),
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            buff = [c * other for c in self.coeffs]
            return Polinomial(buff)
        elif isinstance(other, Polinomial):
            buff = [0] * (self.degr + other.degr + 1)
            for i in range(self.degr + 1):
                for j in range(other.degr + 1):
                    buff[i + j] = buff[i + j] + self.coeffs[i] * other.coeffs[j]
            return Polinomial(buff)
        else:
            raise ValueError

    def __rmul__(self, other):
        return self * other

    # сравнение (==), сравнение с константой (с обеих сторон),
    def __eq__(self, other):
        return self.coeffs == other.coeffs

    # печать внутреннего представления объекта repr(p) в стиле "Polynomial([1, 2, -4])",
    def __repr__(self):
        return f'Polynomial({str(self.coeffs)})'

    # список коэффициентов (list) можно получать/модифицировать как p.coeffs.
    # В случае недопустимых значений или типов входных данных должны выбрасываться соответствующие исключения.
    def __getattr__(self, attrname):
        #print(f'Атрибута {attrname} не существует!')
        raise AttributeError
