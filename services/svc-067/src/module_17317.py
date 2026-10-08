"""Service module 17317: business logic, no crypto."""


def calculate_total_17317(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17317():
    return 'module 17317 handles orders and invoices'
