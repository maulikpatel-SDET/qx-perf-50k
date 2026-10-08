"""Service module 34372: business logic, no crypto."""


def calculate_total_34372(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34372():
    return 'module 34372 handles orders and invoices'
