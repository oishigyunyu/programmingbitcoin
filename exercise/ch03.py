def on_curve(x, y):
    prime = 223
    left = y**2 % prime
    right = (x**3 + 7) % prime
    return left == right


if __name__ == '__main__':
    print(on_curve(192, 105))
    print(on_curve(12, 56))
    print(on_curve(200, 119))
    print(on_curve(1, 193))
    print(on_curve(42, 99))
