"""Service module 7816: business logic, no crypto."""


def calculate_total_7816(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7816():
    return 'module 7816 handles orders and invoices'
