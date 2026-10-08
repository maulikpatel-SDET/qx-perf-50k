"""Service module 19906: business logic, no crypto."""


def calculate_total_19906(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19906():
    return 'module 19906 handles orders and invoices'
