"""Service module 8765: business logic, no crypto."""


def calculate_total_8765(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8765():
    return 'module 8765 handles orders and invoices'
