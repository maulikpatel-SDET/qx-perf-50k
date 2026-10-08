"""Service module 23908: business logic, no crypto."""


def calculate_total_23908(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23908():
    return 'module 23908 handles orders and invoices'
