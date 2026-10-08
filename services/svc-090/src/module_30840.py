"""Service module 30840: business logic, no crypto."""


def calculate_total_30840(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30840():
    return 'module 30840 handles orders and invoices'
