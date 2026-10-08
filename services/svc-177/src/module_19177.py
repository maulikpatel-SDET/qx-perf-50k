"""Service module 19177: business logic, no crypto."""


def calculate_total_19177(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19177():
    return 'module 19177 handles orders and invoices'
