"""Service module 39491: business logic, no crypto."""


def calculate_total_39491(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39491():
    return 'module 39491 handles orders and invoices'
