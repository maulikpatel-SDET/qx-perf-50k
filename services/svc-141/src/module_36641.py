"""Service module 36641: business logic, no crypto."""


def calculate_total_36641(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36641():
    return 'module 36641 handles orders and invoices'
