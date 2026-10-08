"""Service module 28601: business logic, no crypto."""


def calculate_total_28601(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28601():
    return 'module 28601 handles orders and invoices'
