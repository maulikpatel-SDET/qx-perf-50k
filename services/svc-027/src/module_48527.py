"""Service module 48527: business logic, no crypto."""


def calculate_total_48527(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48527():
    return 'module 48527 handles orders and invoices'
