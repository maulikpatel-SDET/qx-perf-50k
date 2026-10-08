"""Service module 42548: business logic, no crypto."""


def calculate_total_42548(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42548():
    return 'module 42548 handles orders and invoices'
