"""Service module 23303: business logic, no crypto."""


def calculate_total_23303(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23303():
    return 'module 23303 handles orders and invoices'
