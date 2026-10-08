"""Service module 21937: business logic, no crypto."""


def calculate_total_21937(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21937():
    return 'module 21937 handles orders and invoices'
