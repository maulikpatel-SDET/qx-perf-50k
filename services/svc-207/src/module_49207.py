"""Service module 49207: business logic, no crypto."""


def calculate_total_49207(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49207():
    return 'module 49207 handles orders and invoices'
