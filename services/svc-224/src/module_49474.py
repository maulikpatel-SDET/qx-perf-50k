"""Service module 49474: business logic, no crypto."""


def calculate_total_49474(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49474():
    return 'module 49474 handles orders and invoices'
