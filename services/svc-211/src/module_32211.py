"""Service module 32211: business logic, no crypto."""


def calculate_total_32211(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32211():
    return 'module 32211 handles orders and invoices'
