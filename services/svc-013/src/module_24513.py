"""Service module 24513: business logic, no crypto."""


def calculate_total_24513(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24513():
    return 'module 24513 handles orders and invoices'
