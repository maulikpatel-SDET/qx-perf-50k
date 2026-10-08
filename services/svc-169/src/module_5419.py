"""Service module 5419: business logic, no crypto."""


def calculate_total_5419(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5419():
    return 'module 5419 handles orders and invoices'
