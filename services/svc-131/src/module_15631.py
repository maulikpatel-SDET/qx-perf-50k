"""Service module 15631: business logic, no crypto."""


def calculate_total_15631(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15631():
    return 'module 15631 handles orders and invoices'
