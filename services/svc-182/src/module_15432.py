"""Service module 15432: business logic, no crypto."""


def calculate_total_15432(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15432():
    return 'module 15432 handles orders and invoices'
