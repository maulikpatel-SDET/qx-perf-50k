"""Service module 18372: business logic, no crypto."""


def calculate_total_18372(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18372():
    return 'module 18372 handles orders and invoices'
