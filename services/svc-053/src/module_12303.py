"""Service module 12303: business logic, no crypto."""


def calculate_total_12303(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12303():
    return 'module 12303 handles orders and invoices'
