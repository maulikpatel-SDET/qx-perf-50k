"""Service module 38942: business logic, no crypto."""


def calculate_total_38942(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38942():
    return 'module 38942 handles orders and invoices'
