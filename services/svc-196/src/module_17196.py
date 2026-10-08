"""Service module 17196: business logic, no crypto."""


def calculate_total_17196(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17196():
    return 'module 17196 handles orders and invoices'
