"""Service module 10213: business logic, no crypto."""


def calculate_total_10213(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10213():
    return 'module 10213 handles orders and invoices'
