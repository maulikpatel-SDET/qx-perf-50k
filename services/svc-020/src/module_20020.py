"""Service module 20020: business logic, no crypto."""


def calculate_total_20020(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20020():
    return 'module 20020 handles orders and invoices'
