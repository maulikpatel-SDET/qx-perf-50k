"""Service module 43529: business logic, no crypto."""


def calculate_total_43529(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43529():
    return 'module 43529 handles orders and invoices'
