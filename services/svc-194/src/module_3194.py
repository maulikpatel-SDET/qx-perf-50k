"""Service module 3194: business logic, no crypto."""


def calculate_total_3194(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3194():
    return 'module 3194 handles orders and invoices'
