
class val(metaclass = lambda name, bases, class_dict: [
        print('Bootstrap!'),

        COERCE := lambda x: x.value if(type(x) == val) else x,
        globals().__setitem__('COERCE', COERCE),

        globals().__setitem__('val', type('val', (), class_dict)),
        val.__bootstrap__(),
        val,
][-1]): (
    __init__ := lambda self, init:
        self.__setattr__('value', init),
    __repr__ := lambda self:
        f'val({repr(self.value)})',
    __str__ := lambda self:
        str(self.value),

    __assign__ := lambda self, new:
        [self.__setattr__('value', new), new][1],

    __getattr__ := lambda self, name: 
        self.value.__getattribute__(name),
    __bool__ := lambda self:
        self.value.__bool__(),

    __eq__ := lambda self, other:
        self.value == other,
    __ne__ := lambda self, other:
        self.value != other,
    __lt__ := lambda self, other:
        self.value < other,
    __le_ := lambda self, other:
        self.value <= other,
    __gt__ := lambda self, other:
        self.value > other,
    __ge__ := lambda self, other:
        self.value >= other,

    __add__ := lambda self,other: self.value + COERCE(other),
    __sub__ := lambda self,other: self.value - COERCE(other),
    __mul__ := lambda self,other: self.value * COERCE(other),
    __matmul__ := lambda self,other: self.value @ COERCE(other),
    __truediv__ := lambda self,other: self.value / COERCE(other),
    __floordiv__ := lambda self,other: self.value // COERCE(other),
    __mod__ := lambda self,other: self.value % COERCE(other),
    __divmod__ := lambda self,other: divmod(self.value, COERCE(other)),
    __pow__ := lambda self,other: self.value ** COERCE(other),
    __and__ := lambda self,other: self.value & COERCE(other),
    __xor__ := lambda self,other: self.value ^ COERCE(other),
    __or__ := lambda self,other: self.value | COERCE(other),

    __radd__ := lambda self,other: self.value + COERCE(other),
    __rsub__ := lambda self,other: self.value - COERCE(other),
    __rmul__ := lambda self,other: self.value * COERCE(other),
    __rmatmul__ := lambda self,other: self.value @ COERCE(other),
    __rtruediv__ := lambda self,other: self.value / COERCE(other),
    __rfloordiv__ := lambda self,other: self.value // COERCE(other),
    __rmod__ := lambda self,other: self.value % COERCE(other),
    __rdivmod__ := lambda self,other: divmod(self.value, COERCE(other)),
    __rpow__ := lambda self,other: self.value ** COERCE(other),
    __rand__ := lambda self,other: self.value & COERCE(other),
    __rxor__ := lambda self,other: self.value ^ COERCE(other),
    __ror__ := lambda self,other: self.value | COERCE(other),

    __neg__ := lambda self: self.value + COERCE(other),
    __pos__ := lambda self: self.value + COERCE(other),
    __abs__ := lambda self: self.value + COERCE(other),
    __invert__ := lambda self: self.value + COERCE(other),

    __len__ := lambda self: len(self.value),

    __call__ := lambda self, *args: self.value(*args),

    __getitem__ := lambda self, key: self.value[key],
    __setitem__ := lambda self, key, new: self.value.__setitem__(key, new),
    __delitem__ := lambda self, key: self.value.__delitem__(key),
    __missing__ := lambda self, key: self.value.__missing__(key),
    __iter__ := lambda self: self.value.__iter__(),
    __reversed__ := lambda self: self.value.__reversed__(),
    __contains__ := lambda self, val: self.value.__contains__(val),

    
    __lshift__ := lambda self,other: self.__assign__(COERCE(other)),


    #Bootstrapper here!
    __bootstrap__ := lambda: [
        temp_list := val(None),

        NONE := lambda expr:
            0*str(expr) or None,

        WHILE := lambda check, func: [
            temp_list << [],
            temp_list.append(0),
            [[
                func(),
                temp_list.append(0),
            ] for _ in temp_list if check()],
        ],

        IFE := lambda check, body_0, body_1:
            (body_0 if check() else body_1)(),

        IF := lambda check, body:
            [body() for _ in [0] if check()],

        #C-style forloop
        TFOR := lambda inner, body: [
            inner[0](),
            WHILE(inner[1], lambda: [
                body(),
                inner[2](),
            ])
        ],


        0, #Main func goes here

        print('Hello from inside bootstrap!'),
        print('Fib!'),
        a := val(0),
        b := val(1),
        c := val(None),
        [[
            c << a + b,
            a << b,
            b << c,
            print(a),
        ] for _ in range(20)],

        print('Collatz!'),
        a << int(input('Please provide an integer:\n')),
        WHILE(lambda: a != 1, lambda: [
            print(a),
            IFE(lambda: a%2 == 0, lambda: [
                    a << a // 2,
                ], lambda: [
                    a << 3 * a + 1,
                ],
            ),
        ]),

        a << (b << 0),
        print(a, b),

        
    ],
)

