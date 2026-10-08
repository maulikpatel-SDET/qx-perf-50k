"""Service module 29643: business logic, no crypto."""


def calculate_total_29643(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29643():
    return 'module 29643 handles orders and invoices'
