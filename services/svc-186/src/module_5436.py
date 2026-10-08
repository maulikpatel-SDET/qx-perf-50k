"""Service module 5436: business logic, no crypto."""


def calculate_total_5436(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5436():
    return 'module 5436 handles orders and invoices'
