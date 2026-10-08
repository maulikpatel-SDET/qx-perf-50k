"""Service module 18971: business logic, no crypto."""


def calculate_total_18971(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18971():
    return 'module 18971 handles orders and invoices'
