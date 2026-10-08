"""Service module 24837: business logic, no crypto."""


def calculate_total_24837(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24837():
    return 'module 24837 handles orders and invoices'
