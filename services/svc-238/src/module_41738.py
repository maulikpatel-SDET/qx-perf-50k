"""Service module 41738: business logic, no crypto."""


def calculate_total_41738(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41738():
    return 'module 41738 handles orders and invoices'
