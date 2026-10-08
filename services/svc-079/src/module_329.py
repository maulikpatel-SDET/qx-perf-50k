"""Service module 329: business logic, no crypto."""


def calculate_total_329(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_329():
    return 'module 329 handles orders and invoices'
