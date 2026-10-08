"""Service module 46976: business logic, no crypto."""


def calculate_total_46976(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46976():
    return 'module 46976 handles orders and invoices'
