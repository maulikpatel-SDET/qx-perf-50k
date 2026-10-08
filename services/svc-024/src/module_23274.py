"""Service module 23274: business logic, no crypto."""


def calculate_total_23274(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23274():
    return 'module 23274 handles orders and invoices'
