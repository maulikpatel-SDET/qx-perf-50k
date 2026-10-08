"""Service module 20776: business logic, no crypto."""


def calculate_total_20776(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20776():
    return 'module 20776 handles orders and invoices'
