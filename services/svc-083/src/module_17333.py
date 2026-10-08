"""Service module 17333: business logic, no crypto."""


def calculate_total_17333(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17333():
    return 'module 17333 handles orders and invoices'
