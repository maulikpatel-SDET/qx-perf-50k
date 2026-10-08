"""Service module 5976: business logic, no crypto."""


def calculate_total_5976(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5976():
    return 'module 5976 handles orders and invoices'
