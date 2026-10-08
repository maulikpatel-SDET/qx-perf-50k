"""Service module 26765: business logic, no crypto."""


def calculate_total_26765(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26765():
    return 'module 26765 handles orders and invoices'
