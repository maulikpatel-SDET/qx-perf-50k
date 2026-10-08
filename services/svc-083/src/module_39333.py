"""Service module 39333: business logic, no crypto."""


def calculate_total_39333(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39333():
    return 'module 39333 handles orders and invoices'
