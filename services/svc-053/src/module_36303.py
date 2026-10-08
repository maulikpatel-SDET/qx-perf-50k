"""Service module 36303: business logic, no crypto."""


def calculate_total_36303(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36303():
    return 'module 36303 handles orders and invoices'
