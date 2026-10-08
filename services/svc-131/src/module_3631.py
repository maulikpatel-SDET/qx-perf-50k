"""Service module 3631: business logic, no crypto."""


def calculate_total_3631(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3631():
    return 'module 3631 handles orders and invoices'
