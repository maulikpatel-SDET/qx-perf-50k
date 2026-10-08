"""Service module 40016: business logic, no crypto."""


def calculate_total_40016(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40016():
    return 'module 40016 handles orders and invoices'
