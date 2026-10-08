"""Service module 33372: business logic, no crypto."""


def calculate_total_33372(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33372():
    return 'module 33372 handles orders and invoices'
