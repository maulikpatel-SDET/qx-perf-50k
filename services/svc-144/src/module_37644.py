"""Service module 37644: business logic, no crypto."""


def calculate_total_37644(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37644():
    return 'module 37644 handles orders and invoices'
