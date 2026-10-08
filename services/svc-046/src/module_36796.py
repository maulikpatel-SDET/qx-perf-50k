"""Service module 36796: business logic, no crypto."""


def calculate_total_36796(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36796():
    return 'module 36796 handles orders and invoices'
