"""Service module 28019: business logic, no crypto."""


def calculate_total_28019(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28019():
    return 'module 28019 handles orders and invoices'
