"""Service module 36222: business logic, no crypto."""


def calculate_total_36222(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36222():
    return 'module 36222 handles orders and invoices'
