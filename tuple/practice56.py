from distutils.util import strtobool


t = (1, '2', 3, '4', 5)
str_t = [str(v) for v in t]
int_t = int(''.join(str_t))
print(int_t)