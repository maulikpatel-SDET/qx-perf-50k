"""Service module 43450: business logic, no crypto."""


def calculate_total_43450(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43450():
    return 'module 43450 handles orders and invoices'
