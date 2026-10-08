"""Service module 45363: business logic, no crypto."""


def calculate_total_45363(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45363():
    return 'module 45363 handles orders and invoices'
