"""Service module 39976: business logic, no crypto."""


def calculate_total_39976(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39976():
    return 'module 39976 handles orders and invoices'
