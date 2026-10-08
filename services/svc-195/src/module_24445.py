"""Service module 24445: business logic, no crypto."""


def calculate_total_24445(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24445():
    return 'module 24445 handles orders and invoices'
