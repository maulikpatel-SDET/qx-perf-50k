"""Service module 30976: business logic, no crypto."""


def calculate_total_30976(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30976():
    return 'module 30976 handles orders and invoices'
