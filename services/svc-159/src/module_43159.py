"""Service module 43159: business logic, no crypto."""


def calculate_total_43159(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43159():
    return 'module 43159 handles orders and invoices'
