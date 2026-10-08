"""Service module 11223: business logic, no crypto."""


def calculate_total_11223(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11223():
    return 'module 11223 handles orders and invoices'
