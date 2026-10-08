"""Service module 25247: business logic, no crypto."""


def calculate_total_25247(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25247():
    return 'module 25247 handles orders and invoices'
