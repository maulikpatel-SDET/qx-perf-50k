"""Service module 42445: business logic, no crypto."""


def calculate_total_42445(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42445():
    return 'module 42445 handles orders and invoices'
