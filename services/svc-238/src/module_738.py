"""Service module 738: business logic, no crypto."""


def calculate_total_738(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_738():
    return 'module 738 handles orders and invoices'
