"""Service module 13035: business logic, no crypto."""


def calculate_total_13035(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13035():
    return 'module 13035 handles orders and invoices'
