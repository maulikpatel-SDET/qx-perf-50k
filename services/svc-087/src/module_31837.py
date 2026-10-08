"""Service module 31837: business logic, no crypto."""


def calculate_total_31837(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31837():
    return 'module 31837 handles orders and invoices'
