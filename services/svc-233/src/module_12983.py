"""Service module 12983: business logic, no crypto."""


def calculate_total_12983(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12983():
    return 'module 12983 handles orders and invoices'
