"""Service module 13931: business logic, no crypto."""


def calculate_total_13931(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13931():
    return 'module 13931 handles orders and invoices'
