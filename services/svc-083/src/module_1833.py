"""Service module 1833: business logic, no crypto."""


def calculate_total_1833(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1833():
    return 'module 1833 handles orders and invoices'
