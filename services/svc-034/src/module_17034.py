"""Service module 17034: business logic, no crypto."""


def calculate_total_17034(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17034():
    return 'module 17034 handles orders and invoices'
