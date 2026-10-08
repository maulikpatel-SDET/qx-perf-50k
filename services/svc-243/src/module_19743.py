"""Service module 19743: business logic, no crypto."""


def calculate_total_19743(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19743():
    return 'module 19743 handles orders and invoices'
