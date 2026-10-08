"""Service module 18333: business logic, no crypto."""


def calculate_total_18333(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18333():
    return 'module 18333 handles orders and invoices'
