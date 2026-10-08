"""Service module 28696: business logic, no crypto."""


def calculate_total_28696(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28696():
    return 'module 28696 handles orders and invoices'
