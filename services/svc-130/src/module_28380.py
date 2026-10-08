"""Service module 28380: business logic, no crypto."""


def calculate_total_28380(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28380():
    return 'module 28380 handles orders and invoices'
