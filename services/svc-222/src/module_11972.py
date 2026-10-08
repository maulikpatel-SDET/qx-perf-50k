"""Service module 11972: business logic, no crypto."""


def calculate_total_11972(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11972():
    return 'module 11972 handles orders and invoices'
