"""Service module 833: business logic, no crypto."""


def calculate_total_833(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_833():
    return 'module 833 handles orders and invoices'
