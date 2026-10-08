"""Service module 39303: business logic, no crypto."""


def calculate_total_39303(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39303():
    return 'module 39303 handles orders and invoices'
