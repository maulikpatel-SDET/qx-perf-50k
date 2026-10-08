"""Service module 36372: business logic, no crypto."""


def calculate_total_36372(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36372():
    return 'module 36372 handles orders and invoices'
