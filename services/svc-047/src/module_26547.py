"""Service module 26547: business logic, no crypto."""


def calculate_total_26547(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26547():
    return 'module 26547 handles orders and invoices'
