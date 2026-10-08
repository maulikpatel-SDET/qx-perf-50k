"""Service module 3796: business logic, no crypto."""


def calculate_total_3796(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3796():
    return 'module 3796 handles orders and invoices'
