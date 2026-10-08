"""Service module 38668: business logic, no crypto."""


def calculate_total_38668(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38668():
    return 'module 38668 handles orders and invoices'
