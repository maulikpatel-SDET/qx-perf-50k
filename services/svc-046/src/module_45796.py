"""Service module 45796: business logic, no crypto."""


def calculate_total_45796(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45796():
    return 'module 45796 handles orders and invoices'
