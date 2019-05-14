## python魔术方法



### 字符串相关
- `__str__`
- `__repr__`
- `__format__`
- `__bytes__`

### 数值转换

- `__abs__`
- `__bool__`
- `__complex__`
- `__int__`
- `__float__`
- `__hash__`
- `__index__`

### 集合模拟

- `__len__`
- `__getitem__`
- `__setitem__`
- `__delitem__`
- `__contains__`


### 迭代枚举

- `__iter__`
- `__reversed__`
- `__next__`


### 调用模拟

- `__call__`

### 上下文管理

- `__enter__`
- `__exit__`

### 实例的创建于销毁

- `__new__`
- `__init__`
- `__del__`

### 属性管理

- `__getattr__`
- `__getattribute__`
- `__setattr__`
- `__delattr__`
- `__dir__`

### 属性描述符

- `__get__`
- `__set__`
- `__delete__`

### 类相关服务

- `__prepare__`
- `__instancecheck__`
- `__subclasscheck__`

### 模块导入相关

- `__all__`

### 一元运算符相关

- `__neg__`
- `__pos__`

### 比较运算符

- `__lt__`
- `__le__`
- `__eq__`
- `__ne__`
- `__gt__`
- `__ge__`

### 算术运算符

- `__add__`
- `__sub__`
- `__mul__`
- `__truediv__`
- `__floodiv__`
- `__mod__`
- `__divmod__`
- `__pow__`
- `__round__`

### 反向算术运算符

- `__iadd__`
- `__isub__`
- `__imul__`
- `__itruediv__`
- `__ifloordiv__`
- `__ipow__`

### 位运算符

- `__invert__`
- `__lshift__`
- `__rshift__`
- `__and__`
- `__or__`
- `__xor__`

### 反向位运算符

- `__rlshift__`
- `__rrshift__`
- `__rand__`
- `__rxor__`
- `__ror__`

### 增量赋值位运算符

- `__ilshift__`
- `__irshift__`
- `__iand__`
- `__ixor__`
- `__ior__`