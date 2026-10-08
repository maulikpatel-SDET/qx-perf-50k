"""Service module 15297: business logic, no crypto."""


def calculate_total_15297(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15297():
    return 'module 15297 handles orders and invoices'
