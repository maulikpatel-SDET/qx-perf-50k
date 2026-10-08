"""Service module 28932: business logic, no crypto."""


def calculate_total_28932(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28932():
    return 'module 28932 handles orders and invoices'
