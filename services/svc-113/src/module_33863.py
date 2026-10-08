"""Service module 33863: business logic, no crypto."""


def calculate_total_33863(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33863():
    return 'module 33863 handles orders and invoices'
