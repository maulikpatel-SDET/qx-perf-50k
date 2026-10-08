"""Service module 31646: business logic, no crypto."""


def calculate_total_31646(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31646():
    return 'module 31646 handles orders and invoices'
