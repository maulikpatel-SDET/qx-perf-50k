"""Service module 8971: business logic, no crypto."""


def calculate_total_8971(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8971():
    return 'module 8971 handles orders and invoices'
