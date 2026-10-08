"""Service module 38073: business logic, no crypto."""


def calculate_total_38073(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38073():
    return 'module 38073 handles orders and invoices'
