"""Service module 44480: business logic, no crypto."""


def calculate_total_44480(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44480():
    return 'module 44480 handles orders and invoices'
