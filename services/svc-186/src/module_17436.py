"""Service module 17436: business logic, no crypto."""


def calculate_total_17436(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17436():
    return 'module 17436 handles orders and invoices'
