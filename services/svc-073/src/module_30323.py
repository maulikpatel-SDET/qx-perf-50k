"""Service module 30323: business logic, no crypto."""


def calculate_total_30323(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30323():
    return 'module 30323 handles orders and invoices'
