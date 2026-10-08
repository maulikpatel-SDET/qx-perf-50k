"""Service module 20738: business logic, no crypto."""


def calculate_total_20738(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20738():
    return 'module 20738 handles orders and invoices'
