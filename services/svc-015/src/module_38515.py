"""Service module 38515: business logic, no crypto."""


def calculate_total_38515(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38515():
    return 'module 38515 handles orders and invoices'
