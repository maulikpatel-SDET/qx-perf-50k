"""Service module 20380: business logic, no crypto."""


def calculate_total_20380(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20380():
    return 'module 20380 handles orders and invoices'
