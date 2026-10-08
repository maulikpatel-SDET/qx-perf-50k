"""Service module 25776: business logic, no crypto."""


def calculate_total_25776(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25776():
    return 'module 25776 handles orders and invoices'
