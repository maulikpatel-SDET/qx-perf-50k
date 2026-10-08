"""Service module 4540: business logic, no crypto."""


def calculate_total_4540(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4540():
    return 'module 4540 handles orders and invoices'
