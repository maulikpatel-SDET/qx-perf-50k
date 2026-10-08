"""Service module 19776: business logic, no crypto."""


def calculate_total_19776(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19776():
    return 'module 19776 handles orders and invoices'
