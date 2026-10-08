"""Service module 3784: business logic, no crypto."""


def calculate_total_3784(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3784():
    return 'module 3784 handles orders and invoices'
