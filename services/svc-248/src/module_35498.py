"""Service module 35498: business logic, no crypto."""


def calculate_total_35498(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35498():
    return 'module 35498 handles orders and invoices'
