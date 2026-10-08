"""Service module 11776: business logic, no crypto."""


def calculate_total_11776(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11776():
    return 'module 11776 handles orders and invoices'
