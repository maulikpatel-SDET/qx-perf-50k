"""Service module 7351: business logic, no crypto."""


def calculate_total_7351(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7351():
    return 'module 7351 handles orders and invoices'
