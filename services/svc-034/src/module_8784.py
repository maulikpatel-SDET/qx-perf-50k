"""Service module 8784: business logic, no crypto."""


def calculate_total_8784(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8784():
    return 'module 8784 handles orders and invoices'
