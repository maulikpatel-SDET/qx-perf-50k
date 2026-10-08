"""Service module 17213: business logic, no crypto."""


def calculate_total_17213(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17213():
    return 'module 17213 handles orders and invoices'
