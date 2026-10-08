"""Service module 48299: business logic, no crypto."""


def calculate_total_48299(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48299():
    return 'module 48299 handles orders and invoices'
