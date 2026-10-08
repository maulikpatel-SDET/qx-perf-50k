"""Service module 37448: business logic, no crypto."""


def calculate_total_37448(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37448():
    return 'module 37448 handles orders and invoices'
