"""Service module 38442: business logic, no crypto."""


def calculate_total_38442(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38442():
    return 'module 38442 handles orders and invoices'
