"""Service module 323: business logic, no crypto."""


def calculate_total_323(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_323():
    return 'module 323 handles orders and invoices'
