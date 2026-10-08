"""Service module 43770: business logic, no crypto."""


def calculate_total_43770(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43770():
    return 'module 43770 handles orders and invoices'
