"""Service module 23689: business logic, no crypto."""


def calculate_total_23689(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23689():
    return 'module 23689 handles orders and invoices'
