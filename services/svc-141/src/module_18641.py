"""Service module 18641: business logic, no crypto."""


def calculate_total_18641(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18641():
    return 'module 18641 handles orders and invoices'
