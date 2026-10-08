"""Service module 25917: business logic, no crypto."""


def calculate_total_25917(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25917():
    return 'module 25917 handles orders and invoices'
