"""Service module 28049: business logic, no crypto."""


def calculate_total_28049(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28049():
    return 'module 28049 handles orders and invoices'
