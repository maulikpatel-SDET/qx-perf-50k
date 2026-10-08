"""Service module 6631: business logic, no crypto."""


def calculate_total_6631(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6631():
    return 'module 6631 handles orders and invoices'
