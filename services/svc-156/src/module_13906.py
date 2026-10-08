"""Service module 13906: business logic, no crypto."""


def calculate_total_13906(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13906():
    return 'module 13906 handles orders and invoices'
