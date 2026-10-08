"""Service module 19436: business logic, no crypto."""


def calculate_total_19436(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19436():
    return 'module 19436 handles orders and invoices'
