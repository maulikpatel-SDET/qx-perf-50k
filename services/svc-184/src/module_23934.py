"""Service module 23934: business logic, no crypto."""


def calculate_total_23934(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23934():
    return 'module 23934 handles orders and invoices'
