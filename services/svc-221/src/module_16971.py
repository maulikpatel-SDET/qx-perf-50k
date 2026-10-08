"""Service module 16971: business logic, no crypto."""


def calculate_total_16971(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16971():
    return 'module 16971 handles orders and invoices'
