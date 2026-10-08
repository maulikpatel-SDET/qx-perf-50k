"""Service module 35833: business logic, no crypto."""


def calculate_total_35833(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35833():
    return 'module 35833 handles orders and invoices'
