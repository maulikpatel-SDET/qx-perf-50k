"""Service module 44976: business logic, no crypto."""


def calculate_total_44976(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44976():
    return 'module 44976 handles orders and invoices'
