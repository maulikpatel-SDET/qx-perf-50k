"""Service module 12406: business logic, no crypto."""


def calculate_total_12406(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12406():
    return 'module 12406 handles orders and invoices'
