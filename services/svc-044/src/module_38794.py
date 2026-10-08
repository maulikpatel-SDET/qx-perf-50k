"""Service module 38794: business logic, no crypto."""


def calculate_total_38794(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38794():
    return 'module 38794 handles orders and invoices'
