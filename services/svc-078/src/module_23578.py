"""Service module 23578: business logic, no crypto."""


def calculate_total_23578(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23578():
    return 'module 23578 handles orders and invoices'
