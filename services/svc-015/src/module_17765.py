"""Service module 17765: business logic, no crypto."""


def calculate_total_17765(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17765():
    return 'module 17765 handles orders and invoices'
