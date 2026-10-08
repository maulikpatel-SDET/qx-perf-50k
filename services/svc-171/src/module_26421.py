"""Service module 26421: business logic, no crypto."""


def calculate_total_26421(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26421():
    return 'module 26421 handles orders and invoices'
