"""Service module 33971: business logic, no crypto."""


def calculate_total_33971(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33971():
    return 'module 33971 handles orders and invoices'
