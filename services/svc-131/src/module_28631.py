"""Service module 28631: business logic, no crypto."""


def calculate_total_28631(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28631():
    return 'module 28631 handles orders and invoices'
