"""Service module 31735: business logic, no crypto."""


def calculate_total_31735(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31735():
    return 'module 31735 handles orders and invoices'
