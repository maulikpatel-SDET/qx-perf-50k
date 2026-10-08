"""Service module 16828: business logic, no crypto."""


def calculate_total_16828(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16828():
    return 'module 16828 handles orders and invoices'
