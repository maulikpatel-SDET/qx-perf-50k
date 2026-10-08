"""Service module 3035: business logic, no crypto."""


def calculate_total_3035(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3035():
    return 'module 3035 handles orders and invoices'
