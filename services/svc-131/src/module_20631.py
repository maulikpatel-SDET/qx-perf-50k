"""Service module 20631: business logic, no crypto."""


def calculate_total_20631(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20631():
    return 'module 20631 handles orders and invoices'
