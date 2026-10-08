"""Service module 529: business logic, no crypto."""


def calculate_total_529(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_529():
    return 'module 529 handles orders and invoices'
