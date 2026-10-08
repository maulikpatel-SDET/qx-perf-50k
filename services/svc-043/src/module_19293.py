"""Service module 19293: business logic, no crypto."""


def calculate_total_19293(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19293():
    return 'module 19293 handles orders and invoices'
