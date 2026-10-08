"""Service module 37837: business logic, no crypto."""


def calculate_total_37837(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37837():
    return 'module 37837 handles orders and invoices'
