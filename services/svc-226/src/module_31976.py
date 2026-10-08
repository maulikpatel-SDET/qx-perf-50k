"""Service module 31976: business logic, no crypto."""


def calculate_total_31976(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31976():
    return 'module 31976 handles orders and invoices'
