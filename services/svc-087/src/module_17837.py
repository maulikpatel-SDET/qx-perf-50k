"""Service module 17837: business logic, no crypto."""


def calculate_total_17837(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17837():
    return 'module 17837 handles orders and invoices'
