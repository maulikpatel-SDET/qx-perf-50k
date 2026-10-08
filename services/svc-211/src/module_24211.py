"""Service module 24211: business logic, no crypto."""


def calculate_total_24211(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24211():
    return 'module 24211 handles orders and invoices'
