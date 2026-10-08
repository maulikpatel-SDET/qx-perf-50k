"""Service module 9971: business logic, no crypto."""


def calculate_total_9971(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9971():
    return 'module 9971 handles orders and invoices'
