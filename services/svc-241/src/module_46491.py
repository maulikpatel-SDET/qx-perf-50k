"""Service module 46491: business logic, no crypto."""


def calculate_total_46491(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46491():
    return 'module 46491 handles orders and invoices'
