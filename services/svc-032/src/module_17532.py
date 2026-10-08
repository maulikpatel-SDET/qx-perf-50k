"""Service module 17532: business logic, no crypto."""


def calculate_total_17532(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17532():
    return 'module 17532 handles orders and invoices'
