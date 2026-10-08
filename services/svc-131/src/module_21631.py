"""Service module 21631: business logic, no crypto."""


def calculate_total_21631(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21631():
    return 'module 21631 handles orders and invoices'
