"""Service module 11971: business logic, no crypto."""


def calculate_total_11971(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11971():
    return 'module 11971 handles orders and invoices'
