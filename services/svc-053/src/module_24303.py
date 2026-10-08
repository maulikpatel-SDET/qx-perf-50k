"""Service module 24303: business logic, no crypto."""


def calculate_total_24303(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24303():
    return 'module 24303 handles orders and invoices'
