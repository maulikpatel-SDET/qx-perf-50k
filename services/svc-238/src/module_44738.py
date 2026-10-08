"""Service module 44738: business logic, no crypto."""


def calculate_total_44738(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44738():
    return 'module 44738 handles orders and invoices'
