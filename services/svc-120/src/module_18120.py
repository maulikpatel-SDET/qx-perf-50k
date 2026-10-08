"""Service module 18120: business logic, no crypto."""


def calculate_total_18120(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18120():
    return 'module 18120 handles orders and invoices'
