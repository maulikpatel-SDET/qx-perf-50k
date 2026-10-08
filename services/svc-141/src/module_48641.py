"""Service module 48641: business logic, no crypto."""


def calculate_total_48641(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48641():
    return 'module 48641 handles orders and invoices'
