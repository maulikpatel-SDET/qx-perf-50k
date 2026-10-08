"""Service module 23232: business logic, no crypto."""


def calculate_total_23232(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23232():
    return 'module 23232 handles orders and invoices'
