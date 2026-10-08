"""Service module 30417: business logic, no crypto."""


def calculate_total_30417(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30417():
    return 'module 30417 handles orders and invoices'
