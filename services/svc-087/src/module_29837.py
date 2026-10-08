"""Service module 29837: business logic, no crypto."""


def calculate_total_29837(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29837():
    return 'module 29837 handles orders and invoices'
