"""Service module 31445: business logic, no crypto."""


def calculate_total_31445(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31445():
    return 'module 31445 handles orders and invoices'
