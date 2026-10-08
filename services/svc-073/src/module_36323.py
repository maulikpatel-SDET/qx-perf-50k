"""Service module 36323: business logic, no crypto."""


def calculate_total_36323(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36323():
    return 'module 36323 handles orders and invoices'
