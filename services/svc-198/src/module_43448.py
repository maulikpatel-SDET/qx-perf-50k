"""Service module 43448: business logic, no crypto."""


def calculate_total_43448(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43448():
    return 'module 43448 handles orders and invoices'
