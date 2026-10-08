"""Service module 40642: business logic, no crypto."""


def calculate_total_40642(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40642():
    return 'module 40642 handles orders and invoices'
