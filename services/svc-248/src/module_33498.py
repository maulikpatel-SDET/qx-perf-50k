"""Service module 33498: business logic, no crypto."""


def calculate_total_33498(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33498():
    return 'module 33498 handles orders and invoices'
