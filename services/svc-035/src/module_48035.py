"""Service module 48035: business logic, no crypto."""


def calculate_total_48035(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48035():
    return 'module 48035 handles orders and invoices'
