"""Service module 34641: business logic, no crypto."""


def calculate_total_34641(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34641():
    return 'module 34641 handles orders and invoices'
