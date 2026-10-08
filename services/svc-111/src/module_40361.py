"""Service module 40361: business logic, no crypto."""


def calculate_total_40361(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40361():
    return 'module 40361 handles orders and invoices'
