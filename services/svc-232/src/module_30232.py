"""Service module 30232: business logic, no crypto."""


def calculate_total_30232(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30232():
    return 'module 30232 handles orders and invoices'
