"""Service module 39274: business logic, no crypto."""


def calculate_total_39274(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39274():
    return 'module 39274 handles orders and invoices'
