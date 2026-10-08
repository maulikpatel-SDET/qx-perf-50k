"""Service module 44297: business logic, no crypto."""


def calculate_total_44297(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44297():
    return 'module 44297 handles orders and invoices'
