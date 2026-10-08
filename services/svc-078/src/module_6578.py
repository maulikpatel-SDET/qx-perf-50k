"""Service module 6578: business logic, no crypto."""


def calculate_total_6578(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6578():
    return 'module 6578 handles orders and invoices'
