"""Service module 25328: business logic, no crypto."""


def calculate_total_25328(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25328():
    return 'module 25328 handles orders and invoices'
