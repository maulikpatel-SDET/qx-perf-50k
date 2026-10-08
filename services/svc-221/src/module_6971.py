"""Service module 6971: business logic, no crypto."""


def calculate_total_6971(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6971():
    return 'module 6971 handles orders and invoices'
