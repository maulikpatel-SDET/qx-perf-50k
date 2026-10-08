"""Service module 49738: business logic, no crypto."""


def calculate_total_49738(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49738():
    return 'module 49738 handles orders and invoices'
