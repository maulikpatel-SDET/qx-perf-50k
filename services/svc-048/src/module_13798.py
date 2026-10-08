"""Service module 13798: business logic, no crypto."""


def calculate_total_13798(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13798():
    return 'module 13798 handles orders and invoices'
