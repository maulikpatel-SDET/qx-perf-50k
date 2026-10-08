"""Service module 13840: business logic, no crypto."""


def calculate_total_13840(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13840():
    return 'module 13840 handles orders and invoices'
