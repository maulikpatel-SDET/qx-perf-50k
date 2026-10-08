"""Service module 20019: business logic, no crypto."""


def calculate_total_20019(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20019():
    return 'module 20019 handles orders and invoices'
