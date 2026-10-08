"""Service module 12271: business logic, no crypto."""


def calculate_total_12271(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12271():
    return 'module 12271 handles orders and invoices'
