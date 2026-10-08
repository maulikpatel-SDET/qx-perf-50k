"""Service module 22833: business logic, no crypto."""


def calculate_total_22833(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22833():
    return 'module 22833 handles orders and invoices'
