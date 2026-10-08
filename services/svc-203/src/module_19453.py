"""Service module 19453: business logic, no crypto."""


def calculate_total_19453(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19453():
    return 'module 19453 handles orders and invoices'
