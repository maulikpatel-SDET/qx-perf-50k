"""Service module 29825: business logic, no crypto."""


def calculate_total_29825(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29825():
    return 'module 29825 handles orders and invoices'
