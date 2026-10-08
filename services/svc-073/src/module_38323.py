"""Service module 38323: business logic, no crypto."""


def calculate_total_38323(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38323():
    return 'module 38323 handles orders and invoices'
