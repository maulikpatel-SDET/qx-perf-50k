"""Service module 39380: business logic, no crypto."""


def calculate_total_39380(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39380():
    return 'module 39380 handles orders and invoices'
