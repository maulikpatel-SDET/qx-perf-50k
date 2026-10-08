"""Service module 12899: business logic, no crypto."""


def calculate_total_12899(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12899():
    return 'module 12899 handles orders and invoices'
