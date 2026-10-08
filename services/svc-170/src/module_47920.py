"""Service module 47920: business logic, no crypto."""


def calculate_total_47920(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47920():
    return 'module 47920 handles orders and invoices'
