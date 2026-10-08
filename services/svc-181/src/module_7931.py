"""Service module 7931: business logic, no crypto."""


def calculate_total_7931(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7931():
    return 'module 7931 handles orders and invoices'
