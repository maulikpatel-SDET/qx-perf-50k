"""Service module 30016: business logic, no crypto."""


def calculate_total_30016(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30016():
    return 'module 30016 handles orders and invoices'
