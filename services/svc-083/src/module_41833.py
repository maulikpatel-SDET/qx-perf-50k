"""Service module 41833: business logic, no crypto."""


def calculate_total_41833(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41833():
    return 'module 41833 handles orders and invoices'
