"""Service module 45018: business logic, no crypto."""


def calculate_total_45018(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45018():
    return 'module 45018 handles orders and invoices'
