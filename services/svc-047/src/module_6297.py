"""Service module 6297: business logic, no crypto."""


def calculate_total_6297(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6297():
    return 'module 6297 handles orders and invoices'
