"""Service module 40436: business logic, no crypto."""


def calculate_total_40436(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40436():
    return 'module 40436 handles orders and invoices'
