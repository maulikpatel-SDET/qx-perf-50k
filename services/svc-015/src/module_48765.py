"""Service module 48765: business logic, no crypto."""


def calculate_total_48765(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48765():
    return 'module 48765 handles orders and invoices'
