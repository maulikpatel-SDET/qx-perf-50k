"""Service module 12168: business logic, no crypto."""


def calculate_total_12168(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12168():
    return 'module 12168 handles orders and invoices'
