"""Service module 39631: business logic, no crypto."""


def calculate_total_39631(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39631():
    return 'module 39631 handles orders and invoices'
