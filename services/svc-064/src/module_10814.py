"""Service module 10814: business logic, no crypto."""


def calculate_total_10814(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10814():
    return 'module 10814 handles orders and invoices'
