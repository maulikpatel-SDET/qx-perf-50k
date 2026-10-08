"""Service module 18274: business logic, no crypto."""


def calculate_total_18274(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18274():
    return 'module 18274 handles orders and invoices'
