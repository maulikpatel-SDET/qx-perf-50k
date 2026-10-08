"""Service module 23223: business logic, no crypto."""


def calculate_total_23223(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23223():
    return 'module 23223 handles orders and invoices'
