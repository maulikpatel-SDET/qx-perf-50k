"""Service module 19631: business logic, no crypto."""


def calculate_total_19631(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19631():
    return 'module 19631 handles orders and invoices'
