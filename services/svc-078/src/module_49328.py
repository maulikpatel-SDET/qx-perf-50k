"""Service module 49328: business logic, no crypto."""


def calculate_total_49328(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49328():
    return 'module 49328 handles orders and invoices'
