"""Service module 48549: business logic, no crypto."""


def calculate_total_48549(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48549():
    return 'module 48549 handles orders and invoices'
