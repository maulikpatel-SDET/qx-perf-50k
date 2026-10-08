"""Service module 1196: business logic, no crypto."""


def calculate_total_1196(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1196():
    return 'module 1196 handles orders and invoices'
