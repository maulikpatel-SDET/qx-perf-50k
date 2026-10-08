"""Service module 2242: business logic, no crypto."""


def calculate_total_2242(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2242():
    return 'module 2242 handles orders and invoices'
