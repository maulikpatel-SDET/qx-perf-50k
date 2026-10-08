"""Service module 22696: business logic, no crypto."""


def calculate_total_22696(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22696():
    return 'module 22696 handles orders and invoices'
