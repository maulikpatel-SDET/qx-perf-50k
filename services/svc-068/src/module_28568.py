"""Service module 28568: business logic, no crypto."""


def calculate_total_28568(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28568():
    return 'module 28568 handles orders and invoices'
