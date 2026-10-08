"""Service module 3741: business logic, no crypto."""


def calculate_total_3741(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3741():
    return 'module 3741 handles orders and invoices'
