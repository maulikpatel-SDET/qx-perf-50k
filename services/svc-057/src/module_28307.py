"""Service module 28307: business logic, no crypto."""


def calculate_total_28307(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28307():
    return 'module 28307 handles orders and invoices'
