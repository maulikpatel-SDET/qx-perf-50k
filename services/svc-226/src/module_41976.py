"""Service module 41976: business logic, no crypto."""


def calculate_total_41976(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41976():
    return 'module 41976 handles orders and invoices'
