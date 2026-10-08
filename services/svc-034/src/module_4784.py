"""Service module 4784: business logic, no crypto."""


def calculate_total_4784(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4784():
    return 'module 4784 handles orders and invoices'
