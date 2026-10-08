"""Service module 45693: business logic, no crypto."""


def calculate_total_45693(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45693():
    return 'module 45693 handles orders and invoices'
