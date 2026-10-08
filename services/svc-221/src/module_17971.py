"""Service module 17971: business logic, no crypto."""


def calculate_total_17971(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17971():
    return 'module 17971 handles orders and invoices'
