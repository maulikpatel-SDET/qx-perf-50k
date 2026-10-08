"""Service module 30372: business logic, no crypto."""


def calculate_total_30372(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30372():
    return 'module 30372 handles orders and invoices'
