"""Service module 23020: business logic, no crypto."""


def calculate_total_23020(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23020():
    return 'module 23020 handles orders and invoices'
