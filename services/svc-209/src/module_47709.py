"""Service module 47709: business logic, no crypto."""


def calculate_total_47709(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47709():
    return 'module 47709 handles orders and invoices'
