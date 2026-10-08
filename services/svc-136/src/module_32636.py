"""Service module 32636: business logic, no crypto."""


def calculate_total_32636(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32636():
    return 'module 32636 handles orders and invoices'
