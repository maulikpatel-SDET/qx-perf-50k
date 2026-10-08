"""Service module 49138: business logic, no crypto."""


def calculate_total_49138(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49138():
    return 'module 49138 handles orders and invoices'
