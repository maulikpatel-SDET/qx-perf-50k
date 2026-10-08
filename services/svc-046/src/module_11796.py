"""Service module 11796: business logic, no crypto."""


def calculate_total_11796(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11796():
    return 'module 11796 handles orders and invoices'
