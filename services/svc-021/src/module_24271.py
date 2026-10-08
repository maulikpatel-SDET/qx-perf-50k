"""Service module 24271: business logic, no crypto."""


def calculate_total_24271(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24271():
    return 'module 24271 handles orders and invoices'
