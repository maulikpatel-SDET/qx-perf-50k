"""Service module 39340: business logic, no crypto."""


def calculate_total_39340(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39340():
    return 'module 39340 handles orders and invoices'
