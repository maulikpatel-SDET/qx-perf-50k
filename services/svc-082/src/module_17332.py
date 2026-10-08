"""Service module 17332: business logic, no crypto."""


def calculate_total_17332(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17332():
    return 'module 17332 handles orders and invoices'
