"""Service module 42776: business logic, no crypto."""


def calculate_total_42776(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42776():
    return 'module 42776 handles orders and invoices'
