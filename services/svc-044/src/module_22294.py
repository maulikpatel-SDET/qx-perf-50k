"""Service module 22294: business logic, no crypto."""


def calculate_total_22294(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22294():
    return 'module 22294 handles orders and invoices'
