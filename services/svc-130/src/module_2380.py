"""Service module 2380: business logic, no crypto."""


def calculate_total_2380(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2380():
    return 'module 2380 handles orders and invoices'
