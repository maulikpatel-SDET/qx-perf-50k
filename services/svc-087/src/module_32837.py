"""Service module 32837: business logic, no crypto."""


def calculate_total_32837(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32837():
    return 'module 32837 handles orders and invoices'
