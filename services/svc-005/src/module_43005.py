"""Service module 43005: business logic, no crypto."""


def calculate_total_43005(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43005():
    return 'module 43005 handles orders and invoices'
