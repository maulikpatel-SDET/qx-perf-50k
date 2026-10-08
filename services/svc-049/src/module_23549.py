"""Service module 23549: business logic, no crypto."""


def calculate_total_23549(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23549():
    return 'module 23549 handles orders and invoices'
