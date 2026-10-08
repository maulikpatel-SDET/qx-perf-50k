"""Service module 2765: business logic, no crypto."""


def calculate_total_2765(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2765():
    return 'module 2765 handles orders and invoices'
