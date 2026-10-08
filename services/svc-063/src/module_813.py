"""Service module 813: business logic, no crypto."""


def calculate_total_813(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_813():
    return 'module 813 handles orders and invoices'
