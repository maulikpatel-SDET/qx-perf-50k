"""Service module 5562: business logic, no crypto."""


def calculate_total_5562(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5562():
    return 'module 5562 handles orders and invoices'
