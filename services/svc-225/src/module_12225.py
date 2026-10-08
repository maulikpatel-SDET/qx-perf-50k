"""Service module 12225: business logic, no crypto."""


def calculate_total_12225(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12225():
    return 'module 12225 handles orders and invoices'
