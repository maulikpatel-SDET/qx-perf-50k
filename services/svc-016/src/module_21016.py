"""Service module 21016: business logic, no crypto."""


def calculate_total_21016(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21016():
    return 'module 21016 handles orders and invoices'
