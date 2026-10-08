"""Service module 5796: business logic, no crypto."""


def calculate_total_5796(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5796():
    return 'module 5796 handles orders and invoices'
