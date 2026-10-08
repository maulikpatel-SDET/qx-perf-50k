"""Service module 13474: business logic, no crypto."""


def calculate_total_13474(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13474():
    return 'module 13474 handles orders and invoices'
