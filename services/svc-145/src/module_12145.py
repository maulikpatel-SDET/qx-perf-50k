"""Service module 12145: business logic, no crypto."""


def calculate_total_12145(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12145():
    return 'module 12145 handles orders and invoices'
