"""Service module 4029: business logic, no crypto."""


def calculate_total_4029(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4029():
    return 'module 4029 handles orders and invoices'
