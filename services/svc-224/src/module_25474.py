"""Service module 25474: business logic, no crypto."""


def calculate_total_25474(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25474():
    return 'module 25474 handles orders and invoices'
