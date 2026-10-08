"""Service module 25334: business logic, no crypto."""


def calculate_total_25334(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25334():
    return 'module 25334 handles orders and invoices'
