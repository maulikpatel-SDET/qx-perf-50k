"""Service module 2562: business logic, no crypto."""


def calculate_total_2562(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2562():
    return 'module 2562 handles orders and invoices'
