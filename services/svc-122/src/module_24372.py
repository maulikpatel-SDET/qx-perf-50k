"""Service module 24372: business logic, no crypto."""


def calculate_total_24372(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24372():
    return 'module 24372 handles orders and invoices'
