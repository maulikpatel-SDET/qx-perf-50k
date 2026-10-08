"""Service module 36049: business logic, no crypto."""


def calculate_total_36049(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36049():
    return 'module 36049 handles orders and invoices'
