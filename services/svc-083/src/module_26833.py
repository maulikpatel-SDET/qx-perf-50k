"""Service module 26833: business logic, no crypto."""


def calculate_total_26833(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26833():
    return 'module 26833 handles orders and invoices'
