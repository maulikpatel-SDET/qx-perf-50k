"""Service module 12265: business logic, no crypto."""


def calculate_total_12265(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12265():
    return 'module 12265 handles orders and invoices'
