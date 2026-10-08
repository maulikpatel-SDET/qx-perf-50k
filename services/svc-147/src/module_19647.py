"""Service module 19647: business logic, no crypto."""


def calculate_total_19647(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19647():
    return 'module 19647 handles orders and invoices'
