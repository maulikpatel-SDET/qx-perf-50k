"""Service module 34399: business logic, no crypto."""


def calculate_total_34399(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34399():
    return 'module 34399 handles orders and invoices'
