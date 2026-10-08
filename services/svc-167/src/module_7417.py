"""Service module 7417: business logic, no crypto."""


def calculate_total_7417(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7417():
    return 'module 7417 handles orders and invoices'
