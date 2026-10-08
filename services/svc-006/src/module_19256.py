"""Service module 19256: business logic, no crypto."""


def calculate_total_19256(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19256():
    return 'module 19256 handles orders and invoices'
