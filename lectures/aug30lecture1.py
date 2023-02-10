def say_hello() -> str:
    return "hello"


def say_hello_to(friend: str) -> str:
    return "hello" + " " + friend


result = say_hello()
print(result)

result = say_hello_to("jane")
print(result)
result = say_hello_to(2)
print(result)
