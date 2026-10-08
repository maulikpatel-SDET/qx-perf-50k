"""Service module 37330: business logic, no crypto."""


def calculate_total_37330(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37330():
    return 'module 37330 handles orders and invoices'
