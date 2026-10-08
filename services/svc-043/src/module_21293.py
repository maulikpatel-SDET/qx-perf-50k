"""Service module 21293: business logic, no crypto."""


def calculate_total_21293(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21293():
    return 'module 21293 handles orders and invoices'
