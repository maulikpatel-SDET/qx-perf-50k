"""Service module 33333: business logic, no crypto."""


def calculate_total_33333(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33333():
    return 'module 33333 handles orders and invoices'
