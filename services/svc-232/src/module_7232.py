"""Service module 7232: business logic, no crypto."""


def calculate_total_7232(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7232():
    return 'module 7232 handles orders and invoices'
