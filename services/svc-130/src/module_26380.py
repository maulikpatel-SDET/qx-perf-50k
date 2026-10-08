"""Service module 26380: business logic, no crypto."""


def calculate_total_26380(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26380():
    return 'module 26380 handles orders and invoices'
