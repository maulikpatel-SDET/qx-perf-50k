"""Service module 46477: business logic, no crypto."""


def calculate_total_46477(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46477():
    return 'module 46477 handles orders and invoices'
