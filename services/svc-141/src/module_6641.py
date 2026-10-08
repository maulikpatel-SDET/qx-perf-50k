"""Service module 6641: business logic, no crypto."""


def calculate_total_6641(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6641():
    return 'module 6641 handles orders and invoices'
