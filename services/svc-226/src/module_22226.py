"""Service module 22226: business logic, no crypto."""


def calculate_total_22226(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22226():
    return 'module 22226 handles orders and invoices'
