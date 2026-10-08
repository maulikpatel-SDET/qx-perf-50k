"""Service module 37414: business logic, no crypto."""


def calculate_total_37414(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37414():
    return 'module 37414 handles orders and invoices'
