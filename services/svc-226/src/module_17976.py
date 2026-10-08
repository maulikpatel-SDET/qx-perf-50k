"""Service module 17976: business logic, no crypto."""


def calculate_total_17976(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17976():
    return 'module 17976 handles orders and invoices'
