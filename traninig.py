class Polynomial:

    def __init__(self, input_str):
        self.polynomial_display_string = input_str.replace('**', '^').replace('*', '').replace("x^1+", "x+") \
            .replace("x^1-", "x-").replace('+0', '').replace('-0', '') \
            .replace('+-', '-').replace('-+', '-').replace('--', '+')
        self.expression_str = self.polynomial_display_string.replace('^', '**').replace('x', '*x') \
            .replace("x+", "x^1+").replace("x-", "x^1-").replace(' ', '').replace('-+', '-').replace('-', '+-')

    def derivative(self):
        if '+' not in self.expression_str:
            if "x" in self.expression_str:
                if self.expression_str[0] == '*':
                    self.expression_str = '1' + self.expression_str
                if "x" in self.expression_str and '**' not in self.expression_str:
                    self.expression_str = self.expression_str + '**1'
                constant_multiplier = int(self.expression_str.split('*x**')[0])
                power = int(self.expression_str.split('*x**')[1])
                derivative = (str(constant_multiplier * power) + "*x^" + str(power - 1))
                return Polynomial(derivative)
            else:
                return Polynomial('0')
        elif self.expression_str[0] == '+' and not self.expression_str.count('+') > 1:
            self.expression_str = self.expression_str.replace('-*', '-1*').replace('+*', '+1*')
            if "x" in self.expression_str and '**' not in self.expression_str:
                self.expression_str = self.expression_str + '**1'
            constant_multiplier = int(self.expression_str[1:].split('*x**')[0])
            power = int(self.expression_str[1:].split('*x**')[1])
            derivative = (str(constant_multiplier * power) + "*x^" + str(power - 1))
            return Polynomial(derivative)
        else:
            terms = list(filter(None, self.expression_str.split('+')))
            final_str = ""
            for term in terms:
                if 'x' not in term and '-' in term:
                    term = term[1:]
                poly_object = Polynomial(term)
                final_str += "+" + str(poly_object.derivative().expression_str)
            final_str = final_str[1:] if final_str[0] in ['+', '-', ' '] else final_str
            final_str = final_str.replace('++', '+').replace('+-', '-').replace('-+', '-').replace('--', '-'). \
                replace('+', ' + ').replace('-', ' - ')
            return Polynomial(final_str)


def differentiate(equation, point):
    polinom = Polynomial(equation).derivative().expression_str.replace('x', '(x)').replace('x', f'{point}')
    result = eval(polinom)
    return result

print(differentiate('-7x^5+22x^4-55x^3-94x^2+87x-56', -3))
print(differentiate("12x+2", 3))
print(differentiate("-5x^2+10x+4", 3))


