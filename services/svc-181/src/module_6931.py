"""Service module 6931: business logic, no crypto."""


def calculate_total_6931(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6931():
    return 'module 6931 handles orders and invoices'
