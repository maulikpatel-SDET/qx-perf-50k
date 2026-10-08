"""Service module 13833: business logic, no crypto."""


def calculate_total_13833(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13833():
    return 'module 13833 handles orders and invoices'
