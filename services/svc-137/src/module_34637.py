"""Service module 34637: business logic, no crypto."""


def calculate_total_34637(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34637():
    return 'module 34637 handles orders and invoices'
