"""Service module 20222: business logic, no crypto."""


def calculate_total_20222(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20222():
    return 'module 20222 handles orders and invoices'
