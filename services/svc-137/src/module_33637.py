"""Service module 33637: business logic, no crypto."""


def calculate_total_33637(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33637():
    return 'module 33637 handles orders and invoices'
