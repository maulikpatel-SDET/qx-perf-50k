"""Service module 31303: business logic, no crypto."""


def calculate_total_31303(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31303():
    return 'module 31303 handles orders and invoices'
