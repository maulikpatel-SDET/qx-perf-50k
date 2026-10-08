"""Service module 25325: business logic, no crypto."""


def calculate_total_25325(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25325():
    return 'module 25325 handles orders and invoices'
