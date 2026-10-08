"""Service module 6738: business logic, no crypto."""


def calculate_total_6738(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6738():
    return 'module 6738 handles orders and invoices'
