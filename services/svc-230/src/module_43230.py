"""Service module 43230: business logic, no crypto."""


def calculate_total_43230(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43230():
    return 'module 43230 handles orders and invoices'
