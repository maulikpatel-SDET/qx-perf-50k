"""Service module 40840: business logic, no crypto."""


def calculate_total_40840(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40840():
    return 'module 40840 handles orders and invoices'
