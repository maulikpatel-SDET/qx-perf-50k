"""Service module 33641: business logic, no crypto."""


def calculate_total_33641(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33641():
    return 'module 33641 handles orders and invoices'
