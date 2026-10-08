"""Service module 17644: business logic, no crypto."""


def calculate_total_17644(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17644():
    return 'module 17644 handles orders and invoices'
