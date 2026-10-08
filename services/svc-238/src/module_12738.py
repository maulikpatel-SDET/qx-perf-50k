"""Service module 12738: business logic, no crypto."""


def calculate_total_12738(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12738():
    return 'module 12738 handles orders and invoices'
