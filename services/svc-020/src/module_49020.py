"""Service module 49020: business logic, no crypto."""


def calculate_total_49020(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49020():
    return 'module 49020 handles orders and invoices'
