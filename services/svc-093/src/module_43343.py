"""Service module 43343: business logic, no crypto."""


def calculate_total_43343(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43343():
    return 'module 43343 handles orders and invoices'
