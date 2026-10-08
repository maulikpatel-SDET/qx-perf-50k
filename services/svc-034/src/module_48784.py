"""Service module 48784: business logic, no crypto."""


def calculate_total_48784(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48784():
    return 'module 48784 handles orders and invoices'
