"""Service module 35477: business logic, no crypto."""


def calculate_total_35477(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35477():
    return 'module 35477 handles orders and invoices'
