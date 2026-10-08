"""Service module 19971: business logic, no crypto."""


def calculate_total_19971(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19971():
    return 'module 19971 handles orders and invoices'
