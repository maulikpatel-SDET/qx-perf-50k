"""Service module 25972: business logic, no crypto."""


def calculate_total_25972(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25972():
    return 'module 25972 handles orders and invoices'
