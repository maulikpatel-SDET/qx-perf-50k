"""Service module 25280: business logic, no crypto."""


def calculate_total_25280(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25280():
    return 'module 25280 handles orders and invoices'
