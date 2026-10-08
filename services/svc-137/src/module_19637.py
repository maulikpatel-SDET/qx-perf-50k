"""Service module 19637: business logic, no crypto."""


def calculate_total_19637(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19637():
    return 'module 19637 handles orders and invoices'
