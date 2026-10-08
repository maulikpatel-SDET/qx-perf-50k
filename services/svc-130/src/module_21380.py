"""Service module 21380: business logic, no crypto."""


def calculate_total_21380(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21380():
    return 'module 21380 handles orders and invoices'
