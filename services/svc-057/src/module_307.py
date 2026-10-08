"""Service module 307: business logic, no crypto."""


def calculate_total_307(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_307():
    return 'module 307 handles orders and invoices'
