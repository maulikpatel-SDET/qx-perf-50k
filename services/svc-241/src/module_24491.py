"""Service module 24491: business logic, no crypto."""


def calculate_total_24491(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24491():
    return 'module 24491 handles orders and invoices'
