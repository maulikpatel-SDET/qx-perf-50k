"""Service module 2461: business logic, no crypto."""


def calculate_total_2461(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2461():
    return 'module 2461 handles orders and invoices'
