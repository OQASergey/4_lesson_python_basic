import random, math

a = "hello"
b = "world!"
print(a + ", " + b)

print("{}, {}".format(a, b.upper()))
print("{first}, {second}{second}{second}".format(first = a, second = b))

url = "https://example.com/{ep}"
url_get = url.format(ep = "get")
url_post = url.format(ep = "post")

print(url_get + " " + url_post)

a1 = "1234"
a2 = 1234
assert a1 != a2

assert int(a2) == a2
assert str(a2) == a1