"""Service module 49211: business logic, no crypto."""


def calculate_total_49211(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49211():
    return 'module 49211 handles orders and invoices'
