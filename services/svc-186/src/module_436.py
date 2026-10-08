"""Service module 436: business logic, no crypto."""


def calculate_total_436(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_436():
    return 'module 436 handles orders and invoices'
