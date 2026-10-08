"""Service module 29972: business logic, no crypto."""


def calculate_total_29972(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29972():
    return 'module 29972 handles orders and invoices'
