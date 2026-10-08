"""Service module 13735: business logic, no crypto."""


def calculate_total_13735(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13735():
    return 'module 13735 handles orders and invoices'
