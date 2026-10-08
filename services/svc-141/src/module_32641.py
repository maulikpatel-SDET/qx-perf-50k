"""Service module 32641: business logic, no crypto."""


def calculate_total_32641(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32641():
    return 'module 32641 handles orders and invoices'
