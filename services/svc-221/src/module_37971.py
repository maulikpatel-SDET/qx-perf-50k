"""Service module 37971: business logic, no crypto."""


def calculate_total_37971(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37971():
    return 'module 37971 handles orders and invoices'
