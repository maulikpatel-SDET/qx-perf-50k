"""Service module 49062: business logic, no crypto."""


def calculate_total_49062(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49062():
    return 'module 49062 handles orders and invoices'
