"""Service module 3299: business logic, no crypto."""


def calculate_total_3299(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3299():
    return 'module 3299 handles orders and invoices'
