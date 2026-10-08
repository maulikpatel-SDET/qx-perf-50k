"""Service module 43868: business logic, no crypto."""


def calculate_total_43868(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43868():
    return 'module 43868 handles orders and invoices'
