"""Service module 42562: business logic, no crypto."""


def calculate_total_42562(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42562():
    return 'module 42562 handles orders and invoices'
