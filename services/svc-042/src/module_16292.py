"""Service module 16292: business logic, no crypto."""


def calculate_total_16292(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16292():
    return 'module 16292 handles orders and invoices'
