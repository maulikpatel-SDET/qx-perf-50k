"""Service module 13700: business logic, no crypto."""


def calculate_total_13700(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13700():
    return 'module 13700 handles orders and invoices'
