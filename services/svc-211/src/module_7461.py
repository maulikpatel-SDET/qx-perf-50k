"""Service module 7461: business logic, no crypto."""


def calculate_total_7461(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7461():
    return 'module 7461 handles orders and invoices'
