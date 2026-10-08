"""Service module 41380: business logic, no crypto."""


def calculate_total_41380(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41380():
    return 'module 41380 handles orders and invoices'
