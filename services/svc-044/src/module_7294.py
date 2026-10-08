"""Service module 7294: business logic, no crypto."""


def calculate_total_7294(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7294():
    return 'module 7294 handles orders and invoices'
