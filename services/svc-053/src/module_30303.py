"""Service module 30303: business logic, no crypto."""


def calculate_total_30303(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30303():
    return 'module 30303 handles orders and invoices'
