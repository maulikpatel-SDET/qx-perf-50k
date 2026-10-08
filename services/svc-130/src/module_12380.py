"""Service module 12380: business logic, no crypto."""


def calculate_total_12380(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12380():
    return 'module 12380 handles orders and invoices'
