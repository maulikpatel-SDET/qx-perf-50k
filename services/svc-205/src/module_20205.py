"""Service module 20205: business logic, no crypto."""


def calculate_total_20205(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20205():
    return 'module 20205 handles orders and invoices'
