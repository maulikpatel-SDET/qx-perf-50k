"""Service module 17741: business logic, no crypto."""


def calculate_total_17741(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17741():
    return 'module 17741 handles orders and invoices'
