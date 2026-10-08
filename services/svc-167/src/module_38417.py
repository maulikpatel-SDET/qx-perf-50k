"""Service module 38417: business logic, no crypto."""


def calculate_total_38417(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38417():
    return 'module 38417 handles orders and invoices'
