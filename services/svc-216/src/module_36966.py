"""Service module 36966: business logic, no crypto."""


def calculate_total_36966(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36966():
    return 'module 36966 handles orders and invoices'
