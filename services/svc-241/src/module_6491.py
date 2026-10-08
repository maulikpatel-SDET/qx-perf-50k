"""Service module 6491: business logic, no crypto."""


def calculate_total_6491(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6491():
    return 'module 6491 handles orders and invoices'
