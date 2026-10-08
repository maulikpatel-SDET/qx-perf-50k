"""Service module 44109: business logic, no crypto."""


def calculate_total_44109(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44109():
    return 'module 44109 handles orders and invoices'
