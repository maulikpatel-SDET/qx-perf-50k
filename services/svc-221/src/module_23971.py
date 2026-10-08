"""Service module 23971: business logic, no crypto."""


def calculate_total_23971(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23971():
    return 'module 23971 handles orders and invoices'
