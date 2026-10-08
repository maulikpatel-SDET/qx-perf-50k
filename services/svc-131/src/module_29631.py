"""Service module 29631: business logic, no crypto."""


def calculate_total_29631(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29631():
    return 'module 29631 handles orders and invoices'
