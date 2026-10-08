"""Service module 22631: business logic, no crypto."""


def calculate_total_22631(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22631():
    return 'module 22631 handles orders and invoices'
