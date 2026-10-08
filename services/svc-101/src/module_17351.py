"""Service module 17351: business logic, no crypto."""


def calculate_total_17351(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17351():
    return 'module 17351 handles orders and invoices'
