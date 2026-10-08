"""Service module 3529: business logic, no crypto."""


def calculate_total_3529(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3529():
    return 'module 3529 handles orders and invoices'
