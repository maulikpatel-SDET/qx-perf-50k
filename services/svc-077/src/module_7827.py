"""Service module 7827: business logic, no crypto."""


def calculate_total_7827(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7827():
    return 'module 7827 handles orders and invoices'
