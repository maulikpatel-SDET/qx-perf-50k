"""Service module 5445: business logic, no crypto."""


def calculate_total_5445(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5445():
    return 'module 5445 handles orders and invoices'
