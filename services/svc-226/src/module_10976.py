"""Service module 10976: business logic, no crypto."""


def calculate_total_10976(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10976():
    return 'module 10976 handles orders and invoices'
