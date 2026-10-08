"""Service module 40774: business logic, no crypto."""


def calculate_total_40774(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40774():
    return 'module 40774 handles orders and invoices'
