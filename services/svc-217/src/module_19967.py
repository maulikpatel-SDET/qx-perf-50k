"""Service module 19967: business logic, no crypto."""


def calculate_total_19967(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19967():
    return 'module 19967 handles orders and invoices'
