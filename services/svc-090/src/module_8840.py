"""Service module 8840: business logic, no crypto."""


def calculate_total_8840(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8840():
    return 'module 8840 handles orders and invoices'
