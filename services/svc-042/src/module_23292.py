"""Service module 23292: business logic, no crypto."""


def calculate_total_23292(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23292():
    return 'module 23292 handles orders and invoices'
