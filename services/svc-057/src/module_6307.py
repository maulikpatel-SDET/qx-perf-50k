"""Service module 6307: business logic, no crypto."""


def calculate_total_6307(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6307():
    return 'module 6307 handles orders and invoices'
