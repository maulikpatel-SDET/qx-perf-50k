"""Service module 36491: business logic, no crypto."""


def calculate_total_36491(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36491():
    return 'module 36491 handles orders and invoices'
