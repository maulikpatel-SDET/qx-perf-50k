"""Service module 562: business logic, no crypto."""


def calculate_total_562(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_562():
    return 'module 562 handles orders and invoices'
