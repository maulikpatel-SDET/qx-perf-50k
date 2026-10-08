"""Service module 1971: business logic, no crypto."""


def calculate_total_1971(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1971():
    return 'module 1971 handles orders and invoices'
