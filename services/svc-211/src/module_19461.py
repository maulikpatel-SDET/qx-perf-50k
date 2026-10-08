"""Service module 19461: business logic, no crypto."""


def calculate_total_19461(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19461():
    return 'module 19461 handles orders and invoices'
