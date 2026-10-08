"""Service module 2845: business logic, no crypto."""


def calculate_total_2845(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2845():
    return 'module 2845 handles orders and invoices'
