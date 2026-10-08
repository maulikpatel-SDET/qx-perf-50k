"""Service module 42303: business logic, no crypto."""


def calculate_total_42303(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42303():
    return 'module 42303 handles orders and invoices'
