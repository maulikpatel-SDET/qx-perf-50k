"""Service module 12776: business logic, no crypto."""


def calculate_total_12776(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12776():
    return 'module 12776 handles orders and invoices'
