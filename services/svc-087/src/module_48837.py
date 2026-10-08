"""Service module 48837: business logic, no crypto."""


def calculate_total_48837(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48837():
    return 'module 48837 handles orders and invoices'
