def main():
    print(concatenate("earth", "mars", "venus"))
    print(convert_to_list("apple", "banana", "cherry"))
    print(concatenate2(prefix="hello", suffix="world"))
    print(display(name="John", age=30, city="New York"))
    
def concatenate(*args, sep=" "):
    return sep.join((args))

def convert_to_list(*args):
    return list(args)

# Basically, the *args parameter allows you to pass a tuple as a parameter.
# The **kwargs parameter allows you to pass a dictionary as a parameter.

# example of **kwargs
def concatenate2(**kwargs):
    return kwargs["prefix"] + " " + kwargs["suffix"]

# another example of **kwargs
def display(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def vote(name, age):
    if age < 18:
        print(f"{name} is not eligible to vote.")
    else:
        print(f"{name} is eligible to vote.")

if __name__ == "__main__":
    main()