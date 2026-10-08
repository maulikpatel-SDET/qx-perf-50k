"""Service module 33256: business logic, no crypto."""


def calculate_total_33256(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33256():
    return 'module 33256 handles orders and invoices'
