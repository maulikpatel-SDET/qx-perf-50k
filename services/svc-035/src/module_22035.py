"""Service module 22035: business logic, no crypto."""


def calculate_total_22035(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22035():
    return 'module 22035 handles orders and invoices'
