"""Service module 43481: business logic, no crypto."""


def calculate_total_43481(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43481():
    return 'module 43481 handles orders and invoices'
