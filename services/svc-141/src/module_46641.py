"""Service module 46641: business logic, no crypto."""


def calculate_total_46641(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46641():
    return 'module 46641 handles orders and invoices'
