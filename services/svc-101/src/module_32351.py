"""Service module 32351: business logic, no crypto."""


def calculate_total_32351(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32351():
    return 'module 32351 handles orders and invoices'
