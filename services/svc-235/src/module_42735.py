"""Service module 42735: business logic, no crypto."""


def calculate_total_42735(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42735():
    return 'module 42735 handles orders and invoices'
