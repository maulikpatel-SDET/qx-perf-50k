"""Service module 19417: business logic, no crypto."""


def calculate_total_19417(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19417():
    return 'module 19417 handles orders and invoices'
