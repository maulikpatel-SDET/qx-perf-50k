"""Service module 16310: business logic, no crypto."""


def calculate_total_16310(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16310():
    return 'module 16310 handles orders and invoices'
