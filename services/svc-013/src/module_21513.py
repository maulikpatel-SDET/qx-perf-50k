"""Service module 21513: business logic, no crypto."""


def calculate_total_21513(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21513():
    return 'module 21513 handles orders and invoices'
