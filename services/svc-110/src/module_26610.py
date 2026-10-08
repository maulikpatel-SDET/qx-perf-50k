"""Service module 26610: business logic, no crypto."""


def calculate_total_26610(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26610():
    return 'module 26610 handles orders and invoices'
