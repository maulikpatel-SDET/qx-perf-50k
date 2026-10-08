"""Service module 17019: business logic, no crypto."""


def calculate_total_17019(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17019():
    return 'module 17019 handles orders and invoices'
