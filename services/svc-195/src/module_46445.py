"""Service module 46445: business logic, no crypto."""


def calculate_total_46445(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46445():
    return 'module 46445 handles orders and invoices'
