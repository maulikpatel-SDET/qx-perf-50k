"""Service module 22244: business logic, no crypto."""


def calculate_total_22244(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22244():
    return 'module 22244 handles orders and invoices'
