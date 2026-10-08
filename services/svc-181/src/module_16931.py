"""Service module 16931: business logic, no crypto."""


def calculate_total_16931(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16931():
    return 'module 16931 handles orders and invoices'
