"""Service module 1976: business logic, no crypto."""


def calculate_total_1976(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1976():
    return 'module 1976 handles orders and invoices'
