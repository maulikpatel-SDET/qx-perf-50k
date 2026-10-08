"""Service module 32372: business logic, no crypto."""


def calculate_total_32372(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32372():
    return 'module 32372 handles orders and invoices'
