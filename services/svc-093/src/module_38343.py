"""Service module 38343: business logic, no crypto."""


def calculate_total_38343(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38343():
    return 'module 38343 handles orders and invoices'
