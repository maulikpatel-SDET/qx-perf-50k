"""Service module 31310: business logic, no crypto."""


def calculate_total_31310(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31310():
    return 'module 31310 handles orders and invoices'
