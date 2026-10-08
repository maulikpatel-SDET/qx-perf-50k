"""Service module 31491: business logic, no crypto."""


def calculate_total_31491(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31491():
    return 'module 31491 handles orders and invoices'
