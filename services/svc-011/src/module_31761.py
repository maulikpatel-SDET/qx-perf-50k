"""Service module 31761: business logic, no crypto."""


def calculate_total_31761(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31761():
    return 'module 31761 handles orders and invoices'
