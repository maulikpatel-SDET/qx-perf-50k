"""Service module 30845: business logic, no crypto."""


def calculate_total_30845(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30845():
    return 'module 30845 handles orders and invoices'
