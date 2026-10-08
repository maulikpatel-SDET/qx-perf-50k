"""Service module 15510: business logic, no crypto."""


def calculate_total_15510(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15510():
    return 'module 15510 handles orders and invoices'
