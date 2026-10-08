"""Service module 11330: business logic, no crypto."""


def calculate_total_11330(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11330():
    return 'module 11330 handles orders and invoices'
