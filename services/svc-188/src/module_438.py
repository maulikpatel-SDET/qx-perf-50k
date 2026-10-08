"""Service module 438: business logic, no crypto."""


def calculate_total_438(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_438():
    return 'module 438 handles orders and invoices'
