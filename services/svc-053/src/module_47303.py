"""Service module 47303: business logic, no crypto."""


def calculate_total_47303(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47303():
    return 'module 47303 handles orders and invoices'
