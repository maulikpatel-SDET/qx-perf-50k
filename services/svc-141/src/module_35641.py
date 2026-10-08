"""Service module 35641: business logic, no crypto."""


def calculate_total_35641(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35641():
    return 'module 35641 handles orders and invoices'
