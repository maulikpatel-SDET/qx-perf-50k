"""Service module 7845: business logic, no crypto."""


def calculate_total_7845(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7845():
    return 'module 7845 handles orders and invoices'
