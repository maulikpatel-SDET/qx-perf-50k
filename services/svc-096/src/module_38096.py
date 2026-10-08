"""Service module 38096: business logic, no crypto."""


def calculate_total_38096(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38096():
    return 'module 38096 handles orders and invoices'
